import os.path
import glob
import json



def main(path):

	folders = glob.glob(os.path.join(path, "*.imageset"), recursive=True)

	for folder in folders:
		rename_pdf(folder)

	

def rename_pdf(folder_path):

	images = glob.glob(os.path.join(folder_path, "*.pdf"))

	if len(images) != 1:
		return

	image_name = os.path.splitext(os.path.basename(folder_path))[0]

	with open(os.path.join(folder_path, "Contents.json")) as f:
		data = json.load(f)

	data["images"][0]["filename"] = image_name + ".pdf"

	with open(os.path.join(folder_path, "Contents.json"), "w") as f:
		json.dump(data, f, sort_keys=True, indent=2)

	os.rename(images[0], os.path.join(os.path.dirname(images[0]), image_name + ".pdf"))



if __name__ == "__main__":
	
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("assets")
	args = parser.parse_args()

	main(args.assets)