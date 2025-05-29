# 🔐 PoC Seguridad en Microservicios

Este repositorio contiene una **Prueba de Concepto (PoC)** orientada a demostrar cómo aplicar medidas de seguridad modernas en un entorno de microservicios utilizando **FastAPI** y **Keycloak**.

---

## 🎯 Objetivo del Proyecto

Implementar un microservicio seguro que utilice **OAuth2** y **OpenID Connect** para gestionar la autenticación y autorización de usuarios, cumpliendo con buenas prácticas de arquitectura y protección contra ataques comunes.

---

## 🧩 Arquitectura del Proyecto

El proyecto está organizado siguiendo una **arquitectura en capas**, lo que permite una mejor mantenibilidad, escalabilidad y separación de responsabilidades. Las capas incluyen:

- **`controller/`**: Define los endpoints de la API, recibe solicitudes y delega el procesamiento a la capa `facade`.
- **`facade/`**: Capa de orquestación. Coordina llamadas a los servicios y encapsula la lógica necesaria para responder a los controladores.
- **`service/`**: Implementa la lógica de negocio principal. Realiza llamadas externas y procesa los datos.
- **`utils/`**: Contiene funciones auxiliares, validadores, manejo de tokens y configuración reutilizable.
- **`config/.env`**: Variables de entorno sensibles y configuraciones externas.

---

## ✅ Ventajas de esta Arquitectura

- **Modularidad**: Cada componente cumple una función específica y desacoplada.
- **Escalabilidad**: Permite añadir nuevos servicios o funcionalidades sin afectar el resto del sistema.
- **Testabilidad**: Es fácil de probar por unidad o por integración gracias a la separación de lógica.
- **Reutilización**: Las utilidades y servicios pueden compartirse entre múltiples controladores o módulos.

---

## 🔐 Seguridad Implementada

Esta PoC cubre los siguientes aspectos clave de seguridad en microservicios:

- ✅ Autenticación y autorización con OAuth2 y OpenID Connect.
- ✅ Gestión de identidades con Keycloak.
- ✅ Comunicación segura entre servicios con `TLS/mTLS` (opcionalmente configurable).
- ✅ Gestión de secretos mediante variables de entorno (`.env`).
- ✅ Prevención de ataques comunes como:
  - Inyección SQL
  - Cross Site Scripting (XSS)
  - Cross Site Request Forgery (CSRF)

---

## 🛠️ Tecnologías Utilizadas

- **FastAPI**: Framework principal para el desarrollo del microservicio.
- **Keycloak**: Servidor de identidad para gestionar usuarios y autenticación.
- **Docker & Docker Compose**: Para orquestar el entorno de desarrollo.
- **Uvicorn**: Servidor ASGI para correr la aplicación FastAPI.
- **Python 3.11+**: Lenguaje base del microservicio.

---

## 🚀 Instrucciones de Ejecución

```bash
# Levantar todo el entorno
docker-compose up --build
