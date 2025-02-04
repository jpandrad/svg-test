from PIL import Image
import potrace

# Carregar a imagem e converter para preto e branco
image_path = "./Floresta.png"
image = Image.open(image_path).convert("1")

# Criar um bitmap para vetorização
bitmap = potrace.Bitmap(image)
path = bitmap.trace()

# Gerar código SVG
svg_code = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {} {}">\n'.format(image.width, image.height)

for curve in path:
    d = "M {} {} ".format(curve.start_point.x, curve.start_point.y)
    for segment in curve:
        if segment.is_corner:
            d += "L {} {} ".format(segment.c.x, segment.c.y)
            d += "L {} {} ".format(segment.end_point.x, segment.end_point.y)
        else:
            d += "C {} {} {} {} {} {} ".format(
                segment.c1.x, segment.c1.y, segment.c2.x, segment.c2.y,
                segment.end_point.x, segment.end_point.y
            )
    d += "Z"
    svg_code += '<path d="{}" stroke="black" fill="black"/>\n'.format(d)

svg_code += "</svg>"

# Salvar o SVG
svg_path = "./output.svg"
with open(svg_path, "w") as f:
    f.write(svg_code)

print(f"SVG gerado e salvo em: {svg_path}")