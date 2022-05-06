from html2image import Html2Image
import folium
from time import sleep
import ast


def read_location():
    """Reads String of name/coordinate information from location.txt, then erases the file. Returns the string in the form of a list of dictionaries."""
    while True:
        sleep(1)
        with open('location.txt', 'r+') as file:
            data = file.read()
            if data:
                file.truncate(0)
                data = ast.literal_eval(data)
        return data


def get_map(parsed_data):
    """Takes list of dictionaries and creates Folium map. Creates markers and labels of trail points and exports map as html and png."""
    if not parsed_data:
        return
    hti = Html2Image(
        custom_flags=['--virtual-time-budget=10000'], size=(550, 400))
    map = folium.Map(
        location=[parsed_data[0]["lat"], parsed_data[0]["lon"]],
        width=550,
        height=400,
        zoom_start=10,
        zoom_control=False
    )

    parsed_data = parsed_data[1:]

    bounds = []
    for loc in parsed_data:
        name = loc["name"]
        folium.Marker(
            location=[loc["lat"], loc["lon"]],
            popup=folium.Popup(f"{name}", max_width=len(
                f"name= {name}")*20, show=True)
        ).add_to(map)
        bounds.append([loc["lat"], loc["lon"]])

    map.fit_bounds(bounds, padding=(50, 50))
    map.save("map.html")
    hti.screenshot(html_file="map.html", save_as="map.png")


def write_img_path(path=""):
    with open('map.txt', 'w') as imgpath:
        imgpath.write(f"{path}/CS-361-Microservice/map.png")


def main_driver():
    parsed = read_location()
    get_map(parsed)
    write_img_path()


if __name__ == "__main__":
    main_driver()
