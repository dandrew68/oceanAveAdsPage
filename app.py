from __future__ import annotations

from pathlib import Path

from dash import Dash, html
from flask import render_template_string, send_from_directory


GOOGLE_TAG_ID = "G-N3E492LY10"

app = Dash(__name__, title="Ocean Avenue Double Bay", update_title=None)
app.index_string = f"""
<!DOCTYPE html>
<html>
    <head>
        {{%metas%}}
        <title>{{%title%}}</title>
        {{%favicon%}}
        <script async src="https://www.googletagmanager.com/gtag/js?id={GOOGLE_TAG_ID}"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){{dataLayer.push(arguments);}}
          gtag('js', new Date());
          gtag('config', '{GOOGLE_TAG_ID}');
        </script>
        {{%css%}}
    </head>
    <body>
        {{%app_entry%}}
        <footer>
            {{%config%}}
            {{%scripts%}}
            {{%renderer%}}
        </footer>
    </body>
</html>
"""
server = app.server
photos_dir = Path(__file__).resolve().parent / "photos"


def _static_page(title: str, heading: str, paragraphs: list[str]) -> str:
    return render_template_string(
        """
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <title>{{ title }}</title>
                <link rel="stylesheet" href="/assets/style.css" />
                <script async src="https://www.googletagmanager.com/gtag/js?id={{ tag_id }}"></script>
                <script>
                  window.dataLayer = window.dataLayer || [];
                  function gtag(){dataLayer.push(arguments);}
                  gtag('js', new Date());
                  gtag('config', '{{ tag_id }}');
                </script>
            </head>
            <body>
                <main class="page policy-page">
                    <div class="policy-card">
                        <div class="pill">Ocean Avenue Double Bay</div>
                        <h1>{{ heading }}</h1>
                        {% for paragraph in paragraphs %}
                        <p class="footer-copy">{{ paragraph }}</p>
                        {% endfor %}
                        <div class="policy-nav">
                            <a class="footer-link" href="/">Back to property page</a>
                        </div>
                    </div>
                </main>
            </body>
        </html>
        """,
        title=title,
        heading=heading,
        paragraphs=paragraphs,
        tag_id=GOOGLE_TAG_ID,
    )


def _listing_button(label: str, href: str, class_name: str, element_id: str, analytics_event: str) -> html.A:
    return html.A(
        label,
        href=href,
        target="_blank",
        rel="noopener",
        className=class_name,
        id=element_id,
        **{"data-analytics-event": analytics_event},
    )


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


@server.route("/owner-contact")
def owner_contact_page():
    return _static_page(
        "Owner & Contact | Ocean Avenue Double Bay",
        "Owner & Contact",
        [
            "This website is operated by Auction Crowd Pty Ltd in connection with the marketing of 3/43 Ocean Avenue, Double Bay.",
            "General and privacy enquiries can be sent to auctioncrowd@gmail.com.",
            "This website is an informational property page that links through to the official listings on realestate.com.au and domain.com.au.",
        ],
    )


@server.route("/privacy-policy")
def privacy_policy_page():
    return _static_page(
        "Privacy Policy | Ocean Avenue Double Bay",
        "Privacy Policy",
        [
            "This site uses Google Analytics and Google Ads measurement tools to understand page visits, engagement and clicks through to the official realestate.com.au and domain.com.au listings.",
            "Those services may collect technical information such as your browser, device, IP address, approximate location, referring page, pages viewed and time on site. We use that information to understand campaign performance and improve this property page.",
            "This site does not include a contact form or direct checkout. If you email us, we will use your details only to respond to your enquiry. We do not sell personal information.",
            "If you click through to a third-party site such as realestate.com.au or domain.com.au, their own privacy policies and terms will apply to your use of those services.",
            "If you have a privacy question or request, contact auctioncrowd@gmail.com.",
        ],
    )

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
                            "A large Art Deco apartment in the tightly held Jefferson building. This property delivers a rare blend "
                            "of scale, privacy and refined contemporary style, in the most peaceful spot in Double Bay.",
                            className="lead",
                        ),
                        html.Ul(
                            className="body-copy",
                            children=[
                                html.Li("Set 80m back from the street, surrounded by lush gardens"),
                                html.Li("Newly renovated, soothing neutral tones"),
                                html.Li("High ceilings, leafy greenery all around"),
                                html.Li("3 large bedrooms with custom built-in wardrobes"),
                                html.Li("King-sized main, 2nd bed with ensuite"),
                                html.Li("New eat-in kitchen with a breakfast bar and ample cabinetry"),
                                html.Li("Miele dishwasher and oven"),
                                html.Li("Main bathroom with a bath, separate W.C., and internal laundry cupboard"),
                                html.Li("Exclusive use of a very large laundry with 2 washers and 2 dryers one day per week"),
                                html.Li("Elevator in building"),
                                html.Li("Part ownership of a large store room"),
                                html.Li("Good scramble parking (subject to House Rules)"),
                                html.Li("200m walk to Double Bay village"),
                                html.Li("Short walk to Edgecliff station"),
                            ],
                        ),
                        html.Div(
                            className="cta-row",
                            children=[
                                _listing_button(
                                    "View on realestate.com.au",
                                    "https://www.realestate.com.au/property-apartment-nsw-double+bay-150764056",
                                    "cta rea",
                                    "rea-link",
                                    "rea_clickout",
                                ),
                                _listing_button(
                                    "View on domain.com.au",
                                    "https://www.domain.com.au/3-43-ocean-avenue-double-bay-nsw-2028-2020727766",
                                    "cta domain",
                                    "domain-link",
                                    "domain_clickout",
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
        html.Div(
            className="legal-links",
            children=[
                html.A("Owner & Contact", href="/owner-contact", className="legal-link"),
                html.A("Privacy Policy", href="/privacy-policy", className="legal-link"),
            ],
        ),
    ],
)


if __name__ == "__main__":
    app.run_server(debug=False, host="0.0.0.0", port=8050)
