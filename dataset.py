import os
import json

class ARVIMDataset:
    def __init__(self, root, metadata_file="metadata.json", transform=None):
        self.root = root
        with open(os.path.join(root, metadata_file), "r", encoding="utf-8") as f:
            self.data = json.load(f)
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        file_path = os.path.join(self.root, item["file_path"])

        sample = {
            "id": item["id"],
            "collection_method": item["collection_method"],
            "attack_format": item["attack_format"],
            "attack_purpose": item["attack_purpose"],
            "label": item["label"],
            "modality": item["modality"],
            "file_path": file_path,
        }

        # 可选：这里加视频帧读取
        if self.transform:
            sample["video"] = self.transform(file_path)

        return sample
