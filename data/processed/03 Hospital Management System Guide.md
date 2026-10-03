**MEDCORE HOSPITALS &amp; HEALTHCARE SERVICES PVT. LTD.  
HOSPITAL MANAGEMENT SYSTEM GUIDE**

Operational user guide for authorized MedCore staff

| **Document ID**    | MC-IT-003               |
|--------------------|-------------------------|
| **Version**        | 3.1                     |
| **Effective Date** | 01 September 2026       |
| **Review Cycle**   | Annual                  |
| **Classification** | Internal — Confidential |

## 1. Overview

The Hospital Management System (HMS) is MedCore's operational platform for managing patient registration, appointments, admissions, clinical workflows, billing, discharge and selected administrative processes. Access is role-based and varies by department.

## 2. Access and Login

- Use your assigned MedCore account. Never share credentials with another user.
- Complete multi-factor authentication where enabled.
- Lock the workstation when leaving it unattended.
- Report repeated login failures, suspicious prompts or unexpected account activity to the IT Service Desk.

## 3. User Interface and Navigation

After login, the home screen displays modules available to the user's role. Common navigation areas include Patient Search, Registration, Appointments, Admissions, Clinical Documentation, Billing, Reports and Administration.

| **Interface element**   | **Typical use**                                                       |
|-------------------------|-----------------------------------------------------------------------|
| Global search           | Locate patients, encounters or operational records permitted by role. |
| Task / work queue       | View assigned items requiring action.                                 |
| Patient context panel   | View permitted demographic and encounter context.                     |
| Alerts / notifications  | Review system-generated tasks and workflow notices.                   |
| Reports                 | Run approved operational reports within assigned permissions.         |

## 4. Patient Registration

- Search for an existing patient before creating a new registration to reduce duplicate records.
- Verify demographic and contact information against the approved identification or registration source.
- Use the correct patient identifier and encounter type.
- Do not create test or duplicate patient records in production unless the approved testing procedure requires it.

## 5. Appointment Management

### Creating an Appointment

- Confirm the patient record and service/department.
- Select the appropriate provider, appointment type and available slot.
- Record required referral or preparation information.
- Confirm the appointment and communicate the approved instructions.

### Changing or Cancelling

Changes should preserve the original appointment history where the system supports audit trails. Cancellations should include an appropriate reason and follow department-specific workflow.

## 6. Admission Workflow

Authorized users can initiate an admission by selecting the correct patient, encounter type, admitting unit and responsible service. Required demographic, payer and administrative information should be completed before finalization.

| **Step**             | **Key check**                                             |
|----------------------|-----------------------------------------------------------|
| 1. Patient selection | Confirm correct patient and avoid duplicate registration. |
| 2. Encounter details | Select appropriate admission type and service.            |
| 3. Bed / unit        | Assign according to authorized operational workflow.      |
| 4. Payer information | Validate available coverage and billing information.      |
| 5. Confirmation      | Review entries before completing admission.               |

## 7. Clinical Documentation

Clinical documentation functions are restricted to authorized clinical roles. Users should enter information in the correct patient and encounter context, use approved templates where applicable and avoid copying information that is not current or relevant.

Corrections should use the system's approved amendment or addendum function rather than deleting historical clinical information where audit preservation is required.

## 8. Orders, Results and Reports

- Review orders and results within the correct patient context.
- Use approved workflows for acknowledgement or follow-up of results.
- Export or print reports only when there is a legitimate business or care need and the destination is approved.
- Do not store restricted reports on personal devices or unapproved cloud services.

## 9. Billing and Financial Workflows

Authorized billing users may review charges, invoices, payments, adjustments and approved dispute workflows. Changes to charges or financial records should follow the applicable approval and audit process.

## 10. Discharge

Discharge workflows may include completion of required clinical or administrative documentation, discharge disposition, billing clearance and communication of approved instructions. Users should verify that required fields and tasks are complete before finalizing the encounter.

## 11. Role-Based Access

| **Role**                  | **Typical HMS capabilities**                                                        |
|---------------------------|-------------------------------------------------------------------------------------|
| Front Desk / Registration | Patient registration, demographics, appointments, basic encounter administration.   |
| Nursing                   | Assigned patient context, nursing documentation and task workflows.                 |
| Clinician                 | Clinical documentation, orders and results within assigned scope.                   |
| Billing                   | Charges, invoices, payments and approved financial workflows.                       |
| HIM                       | Record administration and authorized release workflows.                             |
| IT Support                | Technical support functions; patient-data access only when specifically authorized. |

## 12. Data Quality and Security

- Verify patient identity before entering or viewing information.
- Use only your own account and approved devices.
- Do not photograph screens or copy restricted information into personal applications.
- Report suspected duplicate records, incorrect patient linkage, unauthorized access or system anomalies promptly.

## 13. Common Troubleshooting

| **Issue**                 | **First action**                                                                                                          |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Cannot log in             | Verify account status and use the approved password/MFA recovery process; contact Service Desk if unresolved.             |
| Module missing            | Access may be role-restricted; ask the manager or system owner to confirm required access.                                |
| Patient not found         | Check permitted search fields and identifiers; do not create a duplicate without following registration guidance.         |
| Slow / unavailable system | Check approved service-status information and contact IT Service Desk if the issue persists.                              |
| Unexpected data or screen | Stop the task, avoid making changes and report the issue with the patient/encounter context through the approved channel. |

## 14. Support and Escalation

Routine issues should be raised through the IT Service Desk. Suspected security incidents, unauthorized access or data exposure should be reported through the IT Security incident process. Patient-care-impacting outages should be escalated through the designated clinical/operations continuity route.

## 15. Guide Review

The guide is reviewed annually and whenever material HMS modules, workflows, access controls or security requirements change.

## Frequently Asked Questions

### Can I use another employee's account if the system is urgent?

No. Use your assigned account and the approved emergency or access-escalation process.

### What if I open the wrong patient record?

Stop the activity, do not make changes, and report the event according to the applicable privacy/security workflow.

### Can I export a patient report for convenience?

Only when there is a legitimate approved purpose and the export destination and handling method are authorized.