QRFactory – Generador de Códigos QR Personalizados 
¡Crea códigos QR únicos y personalizados con colores, logos y múltiples formatos!      

¿Qué es QRFactory? 
QRFactory  es una aplicación web desarrollada en Python que permite generar códigos QR totalmente personalizados. Con esta herramienta podrás: 

    -> Generar QR para URLs, SMS, WiFi, Correos, Ubicaciones y Contactos (vCard)
    -> Cambiar los colores del fondo y los módulos
    -> Estilos: cuadrados, círculos y puntos
    -> Agregar un logo al centro del QR
    -> Ajustar el tamaño a tus necesidades     

Todo desde una interfaz web amigable gracias a Streamlit . 
Tecnologías usadas 

    -> Python 3 
    -> Streamlit  – Para la interfaz web
    -> qrcode  – Para generar códigos QR
    -> Pillow (PIL)  – Para edición de imágenes
     
Requisitos:

Antes de ejecutar la app, asegúrate de tener instalado lo siguiente: 
    Python 3.x
    pip (gestor de paquetes de Python)
     
Cómo ejecutar el proyecto 

    Clona este repositorio  (o crea una carpeta nueva si solo tienes el archivo .py) 
    bash
      

git clone https://github.com/tu-usuario/qr-factory.git 
cd qr-factory

Instala las dependencias 
pip install streamlit qrcode pillow 

Ejecuta la aplicación  
    streamlit run qr_factory.py     

    Abre tu navegador 
    Se abrirá automáticamente en: http://localhost:8501  
     
Estructura del proyecto  
 

qr-factory/
│
├── qr_factory.py         # Archivo principal de la aplicación
├── README.md             # Este archivo
└── ejemplo-qr.png        # (Opcional) Imagen de muestra para el README
 
 
Contribuciones 
¡Toda ayuda es bienvenida! Si quieres mejorar esta herramienta, agrega nuevas funcionalidades como: 

    Soporte para descarga en SVG
    Generación de QR animados (GIF)
    Integración con APIs
    Traducción a otros idiomas     

Solo abre un Pull Request 😊 
seniorferre@gmail.com

¡Gracias por usar QRFactory! 
