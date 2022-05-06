from html2image import Html2Image
import folium
from time import sleep
import json
import ast


def get_map():
    sleep(1)
    with open('location.txt', 'r+') as file:
        data = file.read()
        # if data:
        #     file.truncate(0)
    parsed_data = ast.literal_eval(data)
    hti = Html2Image(
        custom_flags=['--virtual-time-budget=10000'], size=(600, 400))
    map = folium.Map(
        location=[parsed_data[0]["lat"], parsed_data[0]["lon"]],
        width=600,
        height=400,
        zoom_start=11
    )

    parsed_data = parsed_data[1:]

    bounds = []
    for loc in parsed_data:
        name = loc["name"]
        folium.Marker(
            location=[loc["lat"], loc["lon"]],
            popup=f"{name}",
            icon=folium.DivIcon(
                html=f"""<div style="font-family: Arial; color: black; font-weight: bold">{name}</div>""")
        ).add_to(map)

    map.fit_bounds(bounds, padding=(2, 2))
    map.save("map.html")

    hti.screenshot(html_file="map.html", save_as="map.png")


if __name__ == "__main__":
    get_map()
