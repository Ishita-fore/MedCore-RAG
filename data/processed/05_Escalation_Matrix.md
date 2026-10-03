| Issue                        | Primary Route      | Secondary Route          | Target               | Required Information                          | Control                                                     | Closure Evidence               |
|------------------------------|--------------------|--------------------------|----------------------|-----------------------------------------------|-------------------------------------------------------------|--------------------------------|
| Clinical question or urgency | Clinical Team      | Patient Services         | Same operating cycle | Patient/encounter; request; timing            | Administrative staff do not interpret clinical matters.     | Clinical routing/status        |
| Billing dispute              | Finance            | Patient Services         | 2 working days       | Encounter; disputed item; patient concern     | Use approved billing records and authority.                 | Finance review                 |
| Privacy concern              | Legal & Compliance | Patient Services         | 2 working days       | Concern; affected process; disclosure context | Use approved verification and minimum necessary disclosure. | Compliance status              |
| Facility concern             | Administration     | Patient Services         | 2 working days       | Location; time; description; safety context   | Urgent safety concerns use immediate escalation.            | Facility action                |
| Appointment conflict         | Scheduling Lead    | Patient Services Manager | Same operating cycle | Service; appointment type; requested timing   | Use approved capacity and appointment types.                | Updated appointment            |
| System failure               | IT Support         | Operations               | Immediate            | System; time; impact; affected workflow       | Use downtime process and reconcile after restoration.       | Incident/reconciliation record |

| Control                  | Purpose                      | Owner                | Routine Action                                 | Exception                              | Evidence              | Review Measure            |
|--------------------------|------------------------------|----------------------|------------------------------------------------|----------------------------------------|-----------------------|---------------------------|
| Search before create     | Prevent duplicate identities | Registration         | Search approved identifiers before new record. | Route plausible duplicates to Records. | Search/audit trail    | Duplicate rate            |
| Identity verification    | Confirm correct patient      | Registration         | Compare available identifiers.                 | Stop when identity is uncertain.       | Registration record   | Verification completeness |
| Temporary reconciliation | Close temporary identities   | Records              | Reconcile after restoration or identification. | Track unresolved records.              | Reconciliation record | Open temporary records    |
| Material correction      | Maintain traceability        | Records              | Use controlled correction workflow.            | Escalate material conflicts.           | Correction record     | Correction volume         |
| Downtime reconciliation  | Restore system accuracy      | Registration/Records | Enter and validate offline records.            | Track unresolved items.                | Downtime log          | Reconciliation aging      |

| Category    | First Level      | Escalation               | Target         | Owner            | Required Record              | Closure                  |
|-------------|------------------|--------------------------|----------------|------------------|------------------------------|--------------------------|
| Billing     | Billing Desk     | Finance Manager          | 2 working days | Patient Services | Complaint and billing review | Resolution/status        |
| Appointment | Reception        | Patient Services Manager | 1 working day  | Patient Services | Scheduling reference         | Updated status           |
| Clinical    | Patient Services | Clinical Head            | 1 working day  | Patient Services | Investigation record         | Clinical routing/outcome |
| Facility    | Administration   | Hospital Administrator   | 2 working days | Patient Services | Facility review              | Action record            |
| Privacy     | Patient Services | Legal & Compliance       | 2 working days | Patient Services | Compliance review            | Compliance status        |

| Rule             | Applies To         | Required Check           | Escalation          | Record                | Communication          | Quality Check         |
|------------------|--------------------|--------------------------|---------------------|-----------------------|------------------------|-----------------------|
| New consultation | New patient        | Service and record       | Scheduling Lead     | Appointment reference | Date/time/location     | Correct type          |
| Follow-up        | Existing patient   | Approved interval        | Scheduling/Clinical | Appointment reference | Next-step details      | Duration/type         |
| Diagnostic       | Imaging/lab        | Preparation/prerequisite | Relevant service    | Preparation status    | Approved instructions  | Prerequisite complete |
| Procedure        | Planned procedure  | Prerequisites            | Clinical/Scheduling | Procedure details     | Approved preparation   | Slot suitability      |
| Tele-consult     | Remote             | Technical readiness      | Scheduling Lead     | Communication details | Approved digital route | Contact readiness     |
| Waitlist         | Earlier request    | Preferences              | Scheduling Lead     | Waitlist status       | Approved contact       | Status updated        |
| No-show          | Missed appointment | Rebooking need           | Patient Services    | No-show status        | Approved follow-up     | Follow-up recorded    |