# white‑label full‑stack

A white‑label full‑stack platform for cooperative, community, and faith‑based organisations—tailored here for faith centres.

## 📋 Project Management

This repository uses **GitHub Project Boards** with the **MoSCoW prioritization method** and **Kanban workflow**.

## Overview

This project provides a modular web platform to manage community content, events, churches/locations, maps, and communications. It is designed to be re‑skinned and reused across organisations while keeping core features consistent.

Use case: A faith‑based organisation wants to create a website to list local churches, manage events, and communicate with members via newsletters.

## Project Map

```text
white-label-community-fullstack/
├─ config/                  # Django project config (settings, urls, wsgi/asgi)
├─ home/                    # Core app: pages, events, churches, newsletter
├─ map/                     # Map view + data processing
├─ theme/                   # Tailwind/DaisyUI theme + base template
│  ├─ templates/            # base.html
│  ├─ static/               # compiled static assets
│  └─ static_src/           # Tailwind/PostCSS source
├─ docs/                    # CSV data sources (church locations)
├─ media/                   # user uploads (events images)
├─ staticfiles/             # collected static output (dev/prod)
├─ manage.py                # Django entrypoint
├─ requirements.txt         # Python deps
├─ tailwind.config.js       # Tailwind config
└─ package.json             # Frontend tooling
```

## Tech Stack

- **Backend:** Django 5  
- **Frontend:** Tailwind CSS + DaisyUI  
- **Database:** SQLite (local) / PostgreSQL (production via `DATABASE_URL`)  
- **Maps:** Google Maps API  
- **Deployment:** Gunicorn + WhiteNoise  

## UI/UX

- Clean, accessible layout with a fixed header and footer  
- Tailwind/DaisyUI theming for consistent components  
- Responsive layouts for events and church listings  
- Newsletter modal and inline signup patterns

## Colour Scheme

|                                Fern Green                                 |                              Cal Poly Green                               |                                   Black                                   |                                   Night                                   |                                 Penn Red                                  |
| :-----------------------------------------------------------------------: | :-----------------------------------------------------------------------: | :-----------------------------------------------------------------------: | :-----------------------------------------------------------------------: | :-----------------------------------------------------------------------: |
| ![#608351](https://via.placeholder.com/30/608351/FFFFFF?text=+) `#608351` | ![#2D3D26](https://via.placeholder.com/30/2D3D26/FFFFFF?text=+) `#2D3D26` | ![#000000](https://via.placeholder.com/30/000000/FFFFFF?text=+) `#000000` | ![#10150D](https://via.placeholder.com/30/10150D/FFFFFF?text=+) `#10150D` | ![#941100](https://via.placeholder.com/30/941100/FFFFFF?text=+) `#941100` |

## Features

- Event management (create, edit, delete, feature)  
- Church directory with contact and location info  
- Newsletter subscription with double opt‑in  
- Map view for locations  
- Contact form with email delivery  

## Quickstart

*(Add setup steps here)*

## Configuration

*(Add environment/configuration notes here)*

## Environment Variables

*(Add required variables here)*

## Running Tests

*(Add test commands here)*

## Deployment

*(Add deployment steps here)*

## Screenshots

*(Add screenshots here)*

## Roadmap

*(Add roadmap here)*

## Contributing

*(Add contributing guidelines here)*

## License

*(Add license info here)*

## Thanks

*(Add acknowledgements here)*
