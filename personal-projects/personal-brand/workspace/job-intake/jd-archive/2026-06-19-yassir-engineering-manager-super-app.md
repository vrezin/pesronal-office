# Yassir - Engineering Manager

- Source: Y Combinator / Work at a Startup
- Captured: 2026-06-19
- Company: Yassir (W20)
- Role: Engineering Manager
- Location: US / Remote
- Employment: Full-time
- Citizenship/visa: US citizenship/visa not required
- Experience: 6+ years
- Status: captured for review

## Company

Yassir is described as the leading super app for French-speaking Africa, currently available in Algeria, Morocco and Tunisia.

The company uses on-demand services such as ride hailing and last-mile delivery to solve immediate user needs and build trust, then use that trust to fuel financial services for a largely underserved and unbanked population.

The posting states that more than 80% of the target population is unbanked and lacks large-scale on-demand services.

## Role

Yassir is looking for an Engineering Manager to lead the engineering department and help build products. The role also includes managing infrastructure and ensuring internal systems operate securely and effectively.

The role includes:

- managing teams;
- setting goals, budgets and timelines;
- owning integrations with external partners;
- overseeing software development plans from ideation to execution.

## Responsibilities

- Oversee front-end and back-end development teams and projects.
- Monitor reliability and performance of internal systems and suggest improvements.
- Ensure compliance with security regulations.
- Manage software development projects by setting requirements, goals and timelines.
- Prepare and manage engineering department budget.
- Design strategies for future development projects based on company objectives and resources.
- Hire engineers and coordinate training.
- Implement innovative technologies.
- Coordinate with external stakeholders for new integrations and tools.
- Review and update policies relevant to internal systems and equipment.

## Requirements

- Engineering manager or similar senior engineering department role.
- Extensive cloud technologies and modern human-computer interfaces experience.
- Hands-on back-end and front-end development experience.
- Good understanding of agile methodologies.
- Leadership abilities with a strategic mind.
- Excellent project-management skills.
- Ideally remote-team management experience.
- BSc/MSc in Engineering, Computer Science or relevant field.

## Technology

Yassir infrastructure is mainly hosted in GCP and relies on many GCP services.

Main architecture components:

- MongoDB / Mongo Atlas fully managed DB cluster, 5 nodes: 1 master, 2 secondary, 1 read-only, 1 BI/Analytics.
- Redis Memory Store as fully managed Redis in GCP, used for caching and Socket.IO queue broker.
- Exposed backend in NodeJS for token authentication, signature verification, role-based authorization and proxying to internal backend.
- Internal backend in NodeJS behind exposed backend, assumes authenticated/authorized requests and communicates directly with MongoDB.
- Socket.IO server for real-time communication, using Redis broker for scalability.
- NodeJS scheduled jobs using Kubernetes Jobs, same codebase as internal backend.
- Google Cloud Functions in NodeJS, triggered by Google Cloud Pub/Sub topics.
- Workers using same codebase as internal backend, parallel processes, Redis-based queue, exactly-once task consumption semantics from the queue design.
- GCP Load Balancer for routing and SSL termination.

Example jobs / async tasks:

- driver invoicing status by month/day;
- scheduled exports;
- resetting monthly consumed balance for B2B users;
- invoice and email attachment generation;
- emails and push notifications;
- trip/order assignment;
- driver/courier location streaming to rider/customer through sockets.
