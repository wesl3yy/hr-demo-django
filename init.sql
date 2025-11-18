-- Organization
INSERT INTO organizations (id, name, description, config)
VALUES ('11111111-1111-1111-1111-111111111111', 'Organization A', 'Technology', '{"allowed_fields": {"department":["name"]}}');

-- Departments
INSERT INTO departments (id, name, description, organization_id)
VALUES
  ('11111111-1111-1111-1111-111111111111', 'Human Resources', 'Handles employee relations and recruitment', '11111111-1111-1111-1111-111111111111'),
  ('11111111-1111-1111-1111-111111111112', 'Finance', 'Manages budgeting and financial operations', '11111111-1111-1111-1111-111111111111'),
  ('11111111-1111-1111-1111-111111111113', 'Engineering', 'Responsible for product development and maintenance', '11111111-1111-1111-1111-111111111111');

-- Employees
INSERT INTO employees (id, first_name, last_name, contact_info)
VALUES
  ('11111111-1111-1111-1111-111111111111', 'John', 'Doe', 'Admin'),
  ('11111111-1111-1111-1111-111111111114', 'Alicia', 'Doe', 'Admin');

-- Locations
INSERT INTO locations (id, name, address, city, organization_id)
VALUES
  ('11111111-1111-1111-1111-111111111115', 'Somewhere', 'in', 'Miami', '11111111-1111-1111-1111-111111111111'),
  ('11111111-1111-1111-1111-111111111116', 'Somewhere', 'in', 'Hanoi', '11111111-1111-1111-1111-111111111111');

-- Positions
INSERT INTO positions (id, name, organization_id)
VALUES
  ('11111111-1111-1111-1111-111111111117', 'Admin', '11111111-1111-1111-1111-111111111111'),
  ('11111111-1111-1111-1111-111111111118', 'Somewhere', '11111111-1111-1111-1111-111111111111');

-- Users
INSERT INTO users (id, first_name, last_name, email, phone, status, organization_id, department_id, location_id, position_id, manager_id)
VALUES
  ('11111111-1111-1111-1111-111111111119', 'John', 'Doe', 'john@example.com', '1234', 't', '11111111-1111-1111-1111-111111111111', '11111111-1111-1111-1111-111111111111', '11111111-1111-1111-1111-111111111115', '11111111-1111-1111-1111-111111111117', NULL),
  ('11111111-1111-1111-1111-111111111120', 'Alicia', 'Doe', 'alicia@example.com', '1234', 't', '11111111-1111-1111-1111-111111111111', '11111111-1111-1111-1111-111111111112', '11111111-1111-1111-1111-111111111116', '11111111-1111-1111-1111-111111111118', NULL);
