# -*- coding: UTF-8 -*-
# generated by lino.sphinxcontrib.help_text_builder
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
help_texts = {
    'lino_voga.lib.courses.desktop.EnrolmentsByCourse' : _("""The Voga version of EnrolmentsByCourse."""),
    'lino_voga.lib.courses.desktop.EnrolmentsByCourse.master' : _("""alias of Course"""),
    'lino_voga.lib.courses.desktop.EnrolmentsByCourse.model' : _("""alias of Enrolment"""),
    'lino_voga.lib.courses.desktop.Pupils' : _("""The global list of all pupils."""),
    'lino_voga.lib.courses.desktop.Pupils.course' : _("""Show only pupils who participate in the given course."""),
    'lino_voga.lib.courses.desktop.Pupils.model' : _("""alias of Pupil"""),
    'lino_voga.lib.courses.desktop.EventsByCourse' : _("""Shows the events linked to this course."""),
    'lino_voga.lib.courses.desktop.EventsByCourse.model' : _("""alias of Event"""),
    'lino_voga.lib.courses.desktop.CourseDetail' : _("""The detail layout of a Course (voga variant)."""),
    'lino_voga.lib.courses.desktop.CoursesByTopic' : _("""Shows the courses of a given topic."""),
    'lino_voga.lib.courses.desktop.CoursesByTopic.master' : _("""alias of Topic"""),
    'lino_voga.lib.courses.desktop.CoursesByTopic.model' : _("""alias of Course"""),
    'lino_voga.lib.courses.desktop.CoursesByLine' : _("""Like lino_cosi.lib.courses.CoursesByLine, but with other
default values in the filter parameters. In Voga we want to see
only courses for which new enrolments can happen."""),
    'lino_voga.lib.courses.desktop.CoursesByLine.master' : _("""alias of Line"""),
    'lino_voga.lib.courses.desktop.CoursesByLine.model' : _("""alias of Course"""),
    'lino_voga.lib.courses.desktop.StatusReport' : _("""Gives an overview about what's up today ."""),
    'lino_voga.lib.courses.desktop.EnrolmentsAndPaymentsByCourse' : _("""Show enrolments of a course together with
invoicing_info and payment_info."""),
    'lino_voga.lib.courses.desktop.EnrolmentsAndPaymentsByCourse.master' : _("""alias of Course"""),
    'lino_voga.lib.courses.desktop.EnrolmentsAndPaymentsByCourse.model' : _("""alias of Enrolment"""),
    'lino_voga.lib.courses.models.PrintPresenceSheet' : _("""Action to print a presence sheet."""),
    'lino_voga.lib.courses.models.CourseToXls' : _("""Interesting, but currently not used."""),
    'lino_voga.lib.courses.models.Teacher' : _("""A teacher is a person with an additional field
teacher_type."""),
    'lino_voga.lib.courses.models.Teacher.teacher_type' : _("""Pointer to TeacherType."""),
    'lino_voga.lib.courses.models.Pupil' : _("""A pupil is a person with an additional field
pupil_type."""),
    'lino_voga.lib.courses.models.Pupil.pupil_type' : _("""Pointer to PupilType."""),
    'lino_voga.lib.courses.models.Course' : _("""Extends the standard model by adding a field fee."""),
    'lino_voga.lib.courses.models.Course.ref' : _("""An identifying public course number to be used by both
external and internal partners for easily referring to a given
course."""),
    'lino_voga.lib.courses.models.Course.name' : _("""A short designation for this course. An extension of the
ref."""),
    'lino_voga.lib.courses.models.Course.line' : _("""Pointer to the course series."""),
    'lino_voga.lib.courses.models.Course.fee' : _("""The default participation fee to apply for new enrolments."""),
    'lino_voga.lib.courses.models.Course.payment_term' : _("""The payment term to use when writing an invoice. If this is
empty, Lino will use the partner's default payment term."""),
    'lino_voga.lib.courses.models.InvoicingInfo' : _("""A volatile object which holds invoicing information about a given
enrolment."""),
    'lino_voga.lib.courses.models.InvoicingInfo.enrolment' : _("""The enrolment it's all about."""),
    'lino_voga.lib.courses.models.InvoicingInfo.max_date' : _("""Don't consider dates after this."""),
    'lino_voga.lib.courses.models.InvoicingInfo.invoiceable_fee' : _("""Which fee to apply. If this is None,"""),
    'lino_voga.lib.courses.models.Enrolment' : _("""Adds"""),
    'lino_voga.lib.courses.models.Enrolment.fee' : _("""The participation fee to apply for this enrolment."""),
    'lino_voga.lib.courses.models.Enrolment.free_events' : _("""Number of events to add for first invoicing for this
enrolment."""),
    'lino_voga.lib.courses.models.Enrolment.amount' : _("""The total amount to pay for this enrolment. This is
places * fee."""),
    'lino_voga.lib.courses.models.Enrolment.pupil_info' : _("""Show the name and address of the participant.  Overrides
lino_cosi.lib.courses.models.Enrolment.pupil_info
in order to add (between parentheses after the name) some
information needed to compute the price."""),
    'lino_voga.lib.courses.models.Enrolment.invoicing_info' : _("""A virtual field showing a summary of recent invoicings."""),
    'lino_voga.lib.courses.models.Enrolment.payment_info' : _("""A virtual field showing a summary of due accounting movements
(debts and payments)."""),
    'lino_voga.lib.invoicing.models.Plan' : _("""An extended invoicing plan."""),
    'lino_voga.lib.invoicing.models.Plan.course' : _("""If this field is nonempty, select only enrolments of that
given course."""),
    'lino_voga.lib.invoicing.models.StartInvoicingForCourse' : _("""Start an invoicing plan for this course."""),
    'lino_voga.lib.voga.migrate.Migrator' : _("""This class is used because a voga Site has
ad.Site.migration_class set to
"lino_voga.migrate.Migrator"."""),
    'lino_voga.projects.roger.lib.courses.models.Pupil' : _("""The Roger variant of Lino Voga adds a few very specific fields
which are being used for filtering, and they may influence the
price of an enrolment."""),
    'lino_voga.projects.roger.lib.courses.models.MemberChecker' : _("""Check membership payments."""),
    'lino_voga.projects.roger.lib.courses.models.MemberChecker.model' : _("""alias of Pupil"""),
    'lino_voga.projects.roger.settings.Site' : _("""The Site class for this module."""),
}
