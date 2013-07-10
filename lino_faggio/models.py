## Copyright 2013 Luc Saffre
## This file is part of the Lino-Faggio project.
## Lino-Faggio is free software; you can redistribute it and/or modify 
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
## Lino-Faggio is distributed in the hope that it will be useful, 
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
## GNU General Public License for more details.
## You should have received a copy of the GNU General Public License
## along with Lino-Faggio; if not, see <http://www.gnu.org/licenses/>.

from django.db import models
from django.db.models import loading
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import string_concat



from lino import dd
from lino import mixins
#~ from lino.models import SiteConfig

#~ from lino.modlib.contacts import models as contacts
#~ from lino.modlib.cal import models as cal

contacts = dd.resolve_app('contacts')
ledger = dd.resolve_app('ledger')
#~ cal = dd.resolve_app('cal')
school = dd.resolve_app('school')
products = dd.resolve_app('products')

#~ print 20130607, loading.cache.postponed

    

#~ dd.inject_field('school.Course',
    #~ 'tariff',
    #~ models.ForeignKey('products.Product',
        #~ blank=True,null=True,
        #~ verbose_name=_("Tariff"),
        #~ related_name='courses_by_tariff'))
        
        
        
class ActiveCourses(school.ActiveCourses):
    app_label = 'school'
    column_names = 'info tariff max_places enrolments teacher company room'
    hide_sums = True

class CourseDetail(school.CourseDetail):     
    main = "general cal.EventsByController"
    general = dd.Panel("""
    line teacher start_date start_time room #slot state id:8
    max_places max_events end_date end_time every_unit every
    monday tuesday wednesday thursday friday saturday sunday
    company contact_person user calendar tariff
    school.EnrolmentsByCourse
    """,label=_("General"))
    

@dd.receiver(dd.post_analyze)
def customize_school(sender,**kw):
    site = sender
    site.modules.school.Courses.set_detail_layout(CourseDetail())
    #~ site.modules.school.ActiveCourses.column_names = 'info tariff max_places enrolments teacher company room'
    

#~ from lino.modlib.cal import models as cal

#~ dd.inject_field('cal.Room','price',dd.PriceField(verbose_name=_("Price"),
    #~ blank=True,null=True,
    #~ default=0))
    
     
class PrintAndChangeStateAction(dd.ChangeStateAction):
    
    def run_from_ui(self,obj,ar,**kw):
        
        def ok():
            # to avoid UnboundLocalError local variable 'kw' referenced before assignment
            kw2 = obj.do_print.run_from_session(ar,**kw)
            kw2 = super(PrintAndChangeStateAction,self).run_from_ui(obj,ar,**kw2)
            kw2.update(refresh_all=True)
            return kw2
        msg = self.get_confirmation_message(obj,ar)
        return ar.confirm(ok, msg, _("Are you sure?"))
    
class ConfirmEnrolment(PrintAndChangeStateAction):
    required = dd.required(states='requested')
    label = _("Confirm")
    
    def get_confirmation_message(self,obj,ar):
        return _("Confirm enrolment of <b>%(pupil)s</b> to <b>%(course)s</b>.") % dict(
            pupil=obj.pupil,course=obj.course)        
    
class CertifyEnrolment(PrintAndChangeStateAction):
    required = dd.required(states='confirmed')
    label = _("Certify")
    #~ label = _("Award")
    #~ label = school.EnrolmentStates.award.text
    
    def get_confirmation_message(self,obj,ar):
        return _("Print certificate for <b>%(pupil)s</b>.") % dict(
            pupil=obj.pupil,course=obj.course)
    

@dd.receiver(dd.pre_analyze,dispatch_uid='faggio_setup_workflows')
def faggio_setup_workflows(sender,**kw):
    
    site = sender
    school = dd.resolve_app('school')

    #~ from lino.modlib.school import models as school
    school.EnrolmentStates.confirmed.add_transition(ConfirmEnrolment)
    school.EnrolmentStates.certified.add_transition(CertifyEnrolment) 
    #~ school.EnrolmentStates.abandoned.add_transition() 


@dd.when_prepared('partners.Person','partners.Organisation')
def hide_region(model):
    model.hide_elements('region')

@dd.when_prepared('partners.Person','partners.Organisation')
def add_merge_action(model):
    model.define_action(merge_row=dd.MergeAction(model))
        
