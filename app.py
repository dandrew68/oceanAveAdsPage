from __future__ import annotations

from pathlib import Path

from dash import Dash, html
from flask import send_from_directory


app = Dash(__name__, title="Ocean Avenue Double Bay", update_title=None)
server = app.server
photos_dir = Path(__file__).resolve().parent / "photos"


def _listing_button(label: str, href: str, class_name: str) -> html.A:
    return html.A(label, href=href, target="_blank", rel="noopener", className=class_name)


def _image_sources() -> list[str]:
    if not photos_dir.exists():
        return []
    allowed = {".png", ".jpg", ".jpeg", ".webp", ".svg"}
    floorplan_names = {"floorplan.png", "floorplan.jpg", "floorplan.jpeg", "floorplan.webp", "floorplan.svg"}
    images = [
        file
        for file in sorted(
            photos_dir.iterdir(),
            key=lambda file: (file.name.lower() in floorplan_names, file.name.lower()),
        )
        if file.is_file() and file.suffix.lower() in allowed
    ]
    return [f"/photos/{file.name}" for file in images]


image_sources = _image_sources()


@server.route("/photos/<path:filename>")
def serve_photo(filename: str):
    return send_from_directory(photos_dir, filename)

app.layout = html.Div(
    className="page",
    children=[
        html.Div(
            className="hero",
            children=[
                html.Div(
                    className="hero-text",
                    children=[
                        html.Div("Apartment for Sale", className="pill"),
                        html.H1("3/43 Ocean Avenue, Double Bay"),
                        html.P(
                            "A house-like Art Deco apartment in the boutique Jefferson building delivers a rare blend "
                            "of scale, privacy and refined contemporary style, in the most peaceful spot in Double Bay.",
                            className="lead",
                        ),
                        html.Ul(
                            className="body-copy",
                            children=[
                                html.Li("Newly renovated, soothing neutral tones"),
                                html.Li("High ceilings, leafy greenery all around"),
                                html.Li("3 large bedrooms with custom built-ins"),
                                html.Li("King-sized main, 2nd bed with ensuite"),
                                html.Li("Stylish eat-in kitchen with a breakfast bar"),
                                html.Li("Miele dishwasher and oven"),
                                html.Li("Main bathroom with a bath, separate W.C."),
                                html.Li("Scramble parking (subject to House Rules)"),
                                html.Li("200m walk to Double Bay village"),
                                html.Li("Stroll to the beach and Double Bay Public School"),
                                html.Li("600m to the ferry or Edgecliff station"),
                            ],
                        ),
                        html.Div(
                            className="cta-row",
                            children=[
                                _listing_button(
                                    "View on realestate.com.au",
                                    "https://www.realestate.com.au/property-apartment-nsw-double+bay-150764056",
                                    "cta rea",
                                ),
                                _listing_button(
                                    "View on domain.com.au",
                                    "https://www.domain.com.au/3-43-ocean-avenue-double-bay-nsw-2028-2020727766",
                                    "cta domain",
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="hero-media",
                    children=[
                        html.Div(
                            className="carousel",
                            **{"data-carousel": "true"},
                            children=[
                                html.Div(
                                    className="carousel-frame",
                                    children=[
                                        *[
                                            html.Img(
                                                src=src,
                                                alt=f"Property photo {index + 1}",
                                                className="carousel-image is-active" if index == 0 else "carousel-image",
                                            )
                                            for index, src in enumerate(image_sources)
                                        ],
                                    ],
                                ),
                                html.Div(
                                    className="carousel-controls",
                                    children=[
                                        html.Button(
                                            "Prev",
                                            className="carousel-btn",
                                            **{
                                                "data-action": "prev",
                                                "aria-label": "Previous photo",
                                                "type": "button",
                                            },
                                        ),
                                        html.Div(
                                            className="carousel-dots",
                                            children=[
                                                *[
                                                    html.Button(
                                                        className="dot is-active" if index == 0 else "dot",
                                                        **{
                                                            "data-index": str(index),
                                                            "aria-label": f"Photo {index + 1}",
                                                            "type": "button",
                                                        },
                                                    )
                                                    for index in range(len(image_sources))
                                                ],
                                            ],
                                        ),
                                        html.Button(
                                            "Next",
                                            className="carousel-btn",
                                            **{
                                                "data-action": "next",
                                                "aria-label": "Next photo",
                                                "type": "button",
                                            },
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        html.Div(
            className="stats-banner",
            children=[
                html.Div(
                    className="stat",
                    children=[
                        html.Img(src="/assets/icons/bed.svg", alt="Beds", className="stat-icon"),
                        html.Div(
                            className="stat-copy",
                            children=[
                                html.Span("3", className="stat-number"),
                                html.Span("Beds", className="stat-label"),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="stat",
                    children=[
                        html.Img(src="/assets/icons/bath.svg", alt="Bathrooms", className="stat-icon"),
                        html.Div(
                            className="stat-copy",
                            children=[
                                html.Span("2", className="stat-number"),
                                html.Span("Bathrooms", className="stat-label"),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="stat",
                    children=[
                        html.Img(src="/assets/icons/car.svg", alt="Car parking", className="stat-icon"),
                        html.Div(
                            className="stat-copy",
                            children=[
                                html.Span("1", className="stat-number"),
                                html.Span("Car park", className="stat-label"),
                                html.Span("Scramble parking", className="stat-note"),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="stat highlight",
                    children=[
                        html.Span("Newly renovated", className="stat-text"),
                    ],
                ),
            ],
        ),
    ],
)


if __name__ == "__main__":
    app.run_server(debug=False, host="0.0.0.0", port=8050)
