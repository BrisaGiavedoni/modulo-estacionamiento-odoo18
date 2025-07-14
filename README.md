![Ubiar Logo](https://media.licdn.com/dms/image/v2/C4D0BAQGmmmyqM7A60g/company-logo_200_200/company-logo_200_200/0/1658158465289/ubiar_logo?e=2147483647&v=beta&t=oeNOv59y7so9jDH-Cpbn6bs2YLIHWz4IU4xUjEdq1xE)


# Módulo de Estacionamiento Odoo 18

Este módulo de Odoo 18 proporciona un sistema básico y funcional para la gestión de estacionamientos, permitiendo registrar la entrada y salida de vehículos, asignar lugares y validar la mensualidad de los clientes.

## Características Principales

* **Registro de Movimientos:** Permite registrar la entrada y salida de vehículos con fecha y hora.
* **Gestión de Lugares:** Asigna vehículos a lugares específicos y valida la disponibilidad de los mismos.
* **Control de Mensualidades:** Verifica si el cliente asociado al vehículo tiene su mensualidad al día antes de permitir el estacionamiento.
* **Visión General del Estado:** Muestra un resumen de la ocupación del estacionamiento (total de lugares, ocupados, libres).
* **Información de Clientes y Vehículos:** Gestión de datos de clientes y sus vehículos asociados.

## Requisitos del Sistema

* Odoo 18.0 (Community o Enterprise Edition)

## Instalación

1.  **Clonar o Descargar el Módulo:**
    * Descarga o clona este repositorio en la carpeta `addons` de tu instancia de Odoo.
    * Por ejemplo: `~/odoo/custom_addons/estacionamiento`

2.  **Actualizar la Lista de Aplicaciones de Odoo:**
    * Inicia tu servidor Odoo.
    * Activa el **Modo Desarrollador** (ve a `Ajustes` y en la parte inferior, haz clic en "Activar el modo desarrollador").
    * Ve a `Aplicaciones` y haz clic en "Actualizar lista de aplicaciones".

3.  **Instalar el Módulo:**
    * En la barra de búsqueda de `Aplicaciones`, busca "Estacionamiento".
    * Haz clic en el botón **"Activar"** (o "Instalar") para instalar el módulo.
    * Si deseas cargar datos de demostración (clientes, vehículos, lugares predefinidos), asegúrate de marcar la casilla **"Load Demo Data"** (Cargar datos de demostración) durante el proceso de instalación si te aparece la opción.

## Uso

Una vez instalado, el módulo "Estacionamiento" aparecerá en el menú principal de Odoo.

* **Clientes:** Gestiona la información de los clientes y su estado de mensualidad.
* **Vehículos:** Registra los vehículos y los asocia a un cliente.
* **Lugares:** Define los espacios de estacionamiento.
* **Movimientos:** Registra la entrada de un vehículo y, posteriormente, su salida. Aquí se realizan las validaciones clave.
* **Estado General:** Consulta la ocupación actual del estacionamiento.

### Proceso de Estacionamiento

1.  **Crear un Cliente:** Asegúrate de que el cliente tenga `Mensualidad al día` marcada si se requiere.
2.  **Crear un Vehículo:** Asocia el vehículo al cliente deseado.
3.  **Crear un Lugar:** Define los espacios disponibles.
4.  **Registrar un Movimiento (Entrada):**
    * Desde el menú "Movimientos", crea uno nuevo.
    * Selecciona el `Cliente`, el `Vehículo` y un `Lugar` disponible (solo se mostrarán los libres).
    * La fecha de entrada se establecerá automáticamente.
    * Selecciona la `Duración`.
    * Al guardar, el sistema validará la mensualidad del cliente y la disponibilidad del lugar.
5.  **Registrar la Salida:**
    * Edita un movimiento existente.
    * Haz clic en el botón **"Registrar salida"** en el formulario del movimiento. Esto actualizará la fecha de salida y liberará el lugar.

## Agradecimientos

Este módulo fue desarrollado como parte de un **desafío de hackathon organizado por Ubiar**.

## Contacto

Si tienes preguntas o necesitas soporte, puedes contactar a:

* Brisa Giavedoni