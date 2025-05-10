import streamlit as st
import qrcode
from PIL import Image, ImageDraw
import io
import base64

# Función para generar QR con círculos
def generate_circle_qr(data, fill_color="black", size=(300, 300)):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    matrix = qr.get_matrix()
    box_size = qr.box_size
    border = qr.border
    width = (len(matrix) + 2 * border) * box_size
    height = width

    img = Image.new("RGBA", (width, height), "white")
    draw = ImageDraw.Draw(img)

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c]:
                x = border * box_size + c * box_size
                y = border * box_size + r * box_size
                draw.ellipse(
                    (x, y, x + box_size, y + box_size),
                    fill=fill_color
                )

    img = img.resize(size, Image.LANCZOS)
    return img

# Interfaz Streamlit
st.title("Generador de Códigos QR Personalizados")

# Selección del tipo de QR
qr_type = st.selectbox("Tipo de QR", ["URL/Texto", "SMS", "Ubicación GPS", "Correo Electrónico", "Red WiFi", "vCard (Contacto)"])

# Campos dinámicos según el tipo de QR
data = ""

if qr_type == "URL/Texto":
    data = st.text_area("Ingresa el texto o URL", value="https://www.ejemplo.com")

elif qr_type == "SMS":
    phone = st.text_input("Número de teléfono (ej: +1234567890)")
    message = st.text_input("Mensaje predeterminado")
    if phone:
        data = f"sms:{phone}?body={message.replace(' ', '%20')}"

elif qr_type == "Ubicación GPS":
    lat = st.text_input("Latitud (ej: 37.7749)")
    lon = st.text_input("Longitud (ej: -122.4194)")
    zoom = st.slider("Zoom (1-21)", 1, 21, 17)
    if lat and lon:
        data = f"geo:{lat},{lon}?z={zoom}"

elif qr_type == "Correo Electrónico":
    email = st.text_input("Correo electrónico")
    subject = st.text_input("Asunto")
    body = st.text_input("Mensaje")
    if email:
        data = f"mailto:{email}?subject={subject.replace(' ', '%20')}&body={body.replace(' ', '%20')}"

elif qr_type == "Red WiFi":
    wifi_name = st.text_input("Nombre de la red (SSID)")
    wifi_pass = st.text_input("Contraseña", type="password")
    wifi_type = st.selectbox("Tipo de red", ["WPA", "WEP", "nopass"])
    if wifi_name:
        data = f"WIFI:S:{wifi_name};T:{wifi_type};P:{wifi_pass};;"

elif qr_type == "vCard (Contacto)":
    name = st.text_input("Nombre completo")
    phone = st.text_input("Teléfono")
    email = st.text_input("Correo")
    company = st.text_input("Empresa")
    website = st.text_input("Sitio web")
    if name:
        data = f"""BEGIN:VCARD
VERSION:3.0
N:{name}
ORG:{company}
TEL;TYPE=CELL:{phone}
EMAIL:{email}
URL:{website}
END:VCARD"""

# Parámetros comunes
fill_color = st.color_picker("Color de los módulos", value="#000000")
back_color = st.color_picker("Color de fondo", value="#FFFFFF")
qr_style = st.selectbox("Estilo del QR", ["Cuadrados", "Círculos", "Puntos"])
size = st.slider("Tamaño del QR", 100, 500, 300)
logo_file = st.file_uploader("Logo opcional (formato PNG)", type=["png"])

submit_button = st.button("Generar QR")

if submit_button and data.strip():
    with st.spinner("Generando QR..."):
        try:
            # Generar QR según estilo
            if qr_type == "vCard (Contacto)":
                qr_img = qrcode.make(data)
            elif qr_style == "Círculos":
                qr_img = generate_circle_qr(data, fill_color=fill_color, size=(size, size))
            else:
                qr_img = qrcode.make(data, fill_color=fill_color, back_color=back_color).convert("RGBA")
                qr_img = qr_img.resize((size, size), Image.LANCZOS)

            # Insertar logo si se proporciona
            if logo_file:
                logo = Image.open(logo_file).convert("RGBA")
                logo_size = min(size // 5, 100)
                logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
                pos = ((qr_img.width - logo.width) // 2, (qr_img.height - logo.height) // 2)
                if qr_style != "Círculos":
                    qr_img.paste(logo, pos, logo)
                else:
                    qr_img.paste(logo, pos, logo)

            # Guardar en memoria para descarga
            img_byte_arr = io.BytesIO()
            qr_img.save(img_byte_arr, format="PNG")
            img_bytes = img_byte_arr.getvalue()

            # Mostrar y descargar
            st.image(img_bytes, caption="Código QR Generado", use_container_width=False)
            b64 = base64.b64encode(img_bytes).decode()
            href = f'<a href="data:image/png;base64,{b64}" download="qr_personalizado.png">📥 Descargar QR</a>'
            st.markdown(href, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error al generar el QR: {e}")
else:
    st.info("Completa los campos para generar el QR.")

# Footer
st.markdown("---")
st.markdown("Creado con ❤️ tiplew.com | Fer Jiménez.")