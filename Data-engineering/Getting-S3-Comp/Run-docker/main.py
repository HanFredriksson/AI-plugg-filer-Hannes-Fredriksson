import src.download_blogs_from_rss as save
import src.extract_articles as load

print("Testing the S3 bucket compatabillty\n")
print("Running test!\n")

blog_name = "mit"
save.main(blog_name)
load.load_metadata(blog_name)

print("The test has ran and was a success!!")
