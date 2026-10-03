| System / Module                           | Front Desk        | Nursing             | Clinician           | Billing           | HIM               | Procurement       | HR                | IT Support    | IT Security      | Access Review   | Data Classification       | Notes                                 |
|-------------------------------------------|-------------------|---------------------|---------------------|-------------------|-------------------|-------------------|-------------------|---------------|------------------|-----------------|---------------------------|---------------------------------------|
| Hospital Management System - Registration | Create / Edit     | View assigned       | View assigned       | View limited      | View / Admin      | No                | No                | Support only  | Support / Audit  | Quarterly       | Restricted                | Patient registration and demographics |
| Hospital Management System - Clinical     | No                | Assigned patient    | Create / Edit       | No                | Authorized review | No                | No                | Support only  | Audit only       | Quarterly       | Restricted                | Clinical notes, orders and results    |
| Hospital Management System - Billing      | Limited view      | No                  | Limited view        | Create / Edit     | Authorized review | No                | No                | Support only  | Audit only       | Quarterly       | Confidential / Restricted | Charges, invoices and payment records |
| Medical Records Repository                | No                | Assigned / approved | Assigned / approved | Limited approved  | Create / Admin    | No                | No                | Support only  | Audit only       | Quarterly       | Restricted                | Formal record access and release      |
| Identity & Access Management              | No                | No                  | No                  | No                | No                | No                | No                | Admin support | Privileged Admin | Monthly         | Restricted                | User lifecycle and role provisioning  |
| Security Monitoring / SIEM                | No                | No                  | No                  | No                | No                | No                | No                | Limited       | Admin            | Monthly         | Restricted                | Security events and logs              |
| Service Desk                              | Submit / view own | Submit / view own   | Submit / view own   | Submit / view own | Submit / view own | Submit / view own | Submit / view own | Agent         | Admin            | Quarterly       | Internal                  | Tickets and support records           |
| Procurement Portal                        | No                | No                  | No                  | No                | No                | Create / Edit     | No                | Support only  | Audit only       | Quarterly       | Confidential              | Supplier and purchase workflow        |
| HR Information System                     | No                | No                  | No                  | No                | No                | No                | Create / Edit     | Support only  | Audit only       | Quarterly       | Restricted                | Employee records                      |
| Document Management System                | View approved     | View approved       | View approved       | View approved     | Edit / Admin      | Edit approved     | Edit approved     | Support only  | Audit only       | Quarterly       | Confidential              | Controlled documents and policies     |

| Level         | Meaning                                                                   |
|---------------|---------------------------------------------------------------------------|
| No            | No routine access.                                                        |
| View assigned | Read access limited to assigned patient/work context.                     |
| View approved | Read access when business purpose and approval exist.                     |
| Create / Edit | Can create or modify records within role scope.                           |
| Admin         | Administrative capability; subject to privileged-access controls.         |
| Support only  | Technical support; data access only when specifically authorized.         |
| Audit only    | Read access for monitoring or investigation; no routine business editing. |

| Access type                   | Review frequency                      | Typical reviewer            |
|-------------------------------|---------------------------------------|-----------------------------|
| Privileged / security admin   | Monthly                               | IT Security / system owner  |
| Sensitive patient-data access | Quarterly                             | System owner / manager      |
| Standard business access      | Quarterly                             | Manager / application owner |
| Vendor access                 | Per contract; quarterly for high-risk | Sponsor / IT Security       |

| Role        | Typical owner                 | Approval note                              |
|-------------|-------------------------------|--------------------------------------------|
| Front Desk  | Patient Services              | Manager approval for application access    |
| Nursing     | Clinical Operations           | Manager / clinical authority               |
| Clinician   | Clinical Operations           | Clinical role validation                   |
| Billing     | Finance & Billing             | Finance manager approval                   |
| HIM         | Health Information Management | HIM manager approval                       |
| Procurement | Procurement                   | Procurement manager approval               |
| HR          | HR & Administration           | HR manager approval                        |
| IT Support  | IT                            | IT manager and privileged-access controls  |
| IT Security | Information Security          | Security lead / privileged access controls |