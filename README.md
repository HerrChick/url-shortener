# Next.js + Flask + SQLAlchemy Template

A modern full-stack web application template using Next.js for the frontend, Flask for the backend, and SQLAlchemy for database management. This template is set up with Docker for easy development and deployment.

## Tech Stack

### Frontend
- Next.js 15.3.1
- React 19
- TypeScript
- TailwindCSS 4
- ESLint for code quality

### Backend
- Flask
- SQLAlchemy (ORM)
- PostgreSQL (via psycopg2)
- Alembic (database migrations)
- Python-dotenv (environment management)

### Development Tools
- Docker and Docker Compose
- TypeScript
- ESLint
- Turbopack (for faster Next.js development)

## Project Structure

```
.
├── frontend/           # Next.js frontend application
│   ├── src/           # Source code
│   ├── public/        # Static assets
│   └── Dockerfile.dev # Development Docker configuration
├── backend/           # Flask backend application
│   ├── db/           # Database models and migrations
│   ├── app.py        # Main Flask application
│   └── Dockerfile.dev # Development Docker configuration
├── docker-compose-dev.yml # Development environment configuration
└── rebuild-dev.sh    # Script to rebuild development containers
```

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Node.js (for local frontend development)
- Python 3.x (for local backend development)

### Development Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd next-flask-sqlalchemy-template
   ```

2. Start the development environment:
   ```bash
   ./rebuild-dev.sh
   ```

This will:
- Build and start the frontend and backend containers
- Set up the development environment
- Start the development servers

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

### Local Development (without Docker)

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Features

- Modern React frontend with Next.js
- Type-safe development with TypeScript
- RESTful API with Flask
- SQLAlchemy ORM for database management
- Dockerized development environment
- Hot reloading for both frontend and backend
- Database migrations with Alembic
- Environment variable management
- Code quality tools (ESLint)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

