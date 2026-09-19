# CultuVivo Events Management System

A terminal-based system for managing cultural events, artists, and attendees — built in Python with a role-based menu (admin, artist, attendee) and JSON file storage. Developed as a team project using Scrum.

---

## 🔄 Features

- Full CRUD for events, artists, and attendees
- Role-based login: admin, artist, or attendee, each with its own menu
- Event registration with date, time, and capacity validation
- Attendee registration and event sign-up, with waitlist ("en espera"), confirmation, and cancellation states
- Automatic capacity enforcement — an event locks itself once it reaches its confirmed-attendee limit
- Assign artists to events, with duplicate-assignment protection
- Reports: artist participation, upcoming events, registered attendees, and lowest-turnout events

---

## 👥 Team

- Scrum Master: Jorge Gomez
- Developer: Felipe Corzo
- Developer: Victor Guzman

---

## 🧩 Scrum methodology

The project was managed under the Scrum framework:

- **Product Backlog:** prioritized user stories (HU1–HU10)
- **Sprint Backlog:** technical tasks derived from the Product Backlog
- **Sprint Review:** review of completed functionality at the end of each sprint
- **Sprint Retrospective:** team performance evaluation and continuous improvement
- **Metrics used:**
  - **Team Velocity (VE):** ratio of completed to planned functionality — `VE = FR / TF`
  - **Estimation Effectiveness (EFC):** accuracy between estimated and actual time — `EFC = TR / TTE`

### Sprint 1 results

| Metric | Result | Interpretation |
|---|---|---|
| Team Velocity (VE) | 1.0 (100%) | All planned stories were completed |
| Estimation Effectiveness (EFC) | 0.85 (85%) | The team finished faster than estimated, with a slight overestimation of hours |

---

## 📎 Documentation

- [Project Management Document (PDF)](docs/project-management.pdf)
- [Product Backlog (Excel)](docs/product-backlog.xlsx)
- [Sprint Planning (Excel)](docs/sprint-planning.xlsx)

---

## 🛠️ Tech stack

- Python 3.8+ (standard library only — `os`, `json`, `datetime`)
- JSON files for local, human-readable data storage
- Git / GitHub for version control

---

## ⚙️ Setup instructions

1. Clone the repo:

```
git clone https://github.com/jorgegmch/cultuvivo-events-system.git
```

2. Run it — no dependencies to install:

```bash
python main.py
```

---

## 🧭 Usage

- From the main menu, register as an attendee or log in with an existing ID.
- **Attendees** can browse events, sign up, check their registrations, confirm/cancel status, and cancel a sign-up entirely.
- **Artists** can view their assigned presentations and event details.
- **Admins** can create events, register artists, assign artists to events, monitor capacity, and pull reports.

---

## 📁 Project structure

```
cultuvivo-events-system
├── data/
│   ├── admins.json
│   ├── artistas.json
│   ├── asignaciones_artistas.json
│   ├── asistentes.json
│   ├── eventos.json
│   └── inscripciones.json
├── docs/
│   ├── project-management.pdf
│   ├── product-backlog.xlsx
│   └── sprint-planning.xlsx
├── modules/
│   ├── CRUD.py
│   ├── messages.py
│   └── utils.py
├── .gitignore
├── LICENSE
├── main.py
└── README.md
```

---

## License

MIT — see [LICENSE](LICENSE) for details.

Built by the CultuVivo team — Jorge Gomez (Scrum Master), Felipe Corzo, Victor Guzman