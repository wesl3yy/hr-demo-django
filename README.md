# Employee Search API

## Prerequisites

- Docker and Docker Compose
- Python 3.11+ (for local development)
- PostgreSQL 15+ (if running without Docker)

## Quick Start

### Using Docker Compose (Recommended)
```bash
docker-compose up -d
```

4. The API will be available at:
- API: http://127.0.0.1:8000
- API Documentation: http://127.0.0.1:8000/docs

## Testing

Run tests with pytest:

```bash
# Unit tests
python3 manage.py test <some_app>
```

## Performance

The API is designed to handle millions of records efficiently:

- **Pagination**: Efficient offset-based pagination
- **Rate Limiting**: Prevents abuse and ensures fair usage

## Security
- **Multi-tenancy**: Complete data isolation between organizations
- **Input Validation**: Comprehensive request validation
- **SQL Injection Prevention**: Parameterized queries
- **Rate Limiting**: Per-tenant request limits
- **CORS**: Configurable CORS policies
