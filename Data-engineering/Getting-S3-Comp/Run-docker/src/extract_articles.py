from bs4 import BeautifulSoup
from s3pathlib import S3Path


path = S3Path(
    "s3://data.lake/",
    endpoint_url="http://127.0.0.1:9000",
    access_key="save.load",
    secret_key="save.load89"
)


def load_metadata(blog_name: str) -> BeautifulSoup:
    # metadata_path = path / blog_name / "metadata.xml"
    # # with open(metadata_path) as f:
    # #     xml_text = f.read()
    s3_file = path / blog_name / "metadata.xml"
    xml_text = s3_file.read_text()
    
    parsed_xml = BeautifulSoup(xml_text, "xml")
    
    return print("Metadata loaded and parsed"), parsed_xml