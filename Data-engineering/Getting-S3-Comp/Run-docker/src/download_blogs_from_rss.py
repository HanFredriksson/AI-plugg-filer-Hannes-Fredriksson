from s3pathlib import S3Path
import requests


LINK_TO_XML_FILE = {
    "mit": "https://news.mit.edu/rss/topic/artificial-intelligence2",
}
path = S3Path(
    "s3://data.lake/",
    endpoint_url="http://127.0.0.1:9000",
    access_key="save.load",
    secret_key="save.load89"
)


def get_metadata_info(blog_name: str) -> str:
    assert (
        blog_name in LINK_TO_XML_FILE
    ), f"{blog_name=} not supported. Supported blogs: {list(LINK_TO_XML_FILE)}"
    blog_url = LINK_TO_XML_FILE[blog_name]
    response = requests.get(blog_url)
    xml_text = response.text
    # xml_text = response.content.decode("utf-8")
    return xml_text


def save_metadata_info(xml_text: str, blog_name: str) -> None:
    # path_xml_dir = Path("data/data_lake") / blog_name
    path_xml_dir = path / blog_name
    path_xml_dir.mkdir(exist_ok=True, parents=True)
    # with open(path_xml_dir / "metadata.xml", "w") as f:
    #     f.write(xml_text)
    # with open(path_xml_dir / "metadata.xml", "w", encoding="utf-8") as f:
    #     f.write(xml_text)
    s3_file = path / blog_name / "metadata.xml"
    s3_file.write_text(xml_text)

def main(blog_name: str) -> None:
    print(f"Processing {blog_name}")
    xml_text = get_metadata_info(blog_name)
    save_metadata_info(xml_text, blog_name)
    print(f"Done processing {blog_name}")