import os

CATEGORIES = {
    "discovery": "discovery_common.txt",
    "fuzzing": "fuzzing_polyglots.txt",
    "api": "api_endpoints.txt",
    "passwords": "passwords_patterns.txt"
}

SRC_DIR = "src"
OUTPUT_DIR = "dist"

def process_file(file_path):
    if not os.path.exists(file_path):
        return []
    
    unique_lines = set()
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            item = line.strip()
            if item and not item.startswith('#'):
                unique_lines.add(item)
    
    # Urutkan dari string terpendek ke terpanjang
    return sorted(list(unique_lines), key=len)

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    print("[*] Memulai kompilasi MRK-SecLists...")
    
    all_combined = set()

    for category, output_name in CATEGORIES.items():
        input_path = os.path.join(SRC_DIR, f"{category}.txt")
        output_path = os.path.join(OUTPUT_DIR, output_name)
        
        cleaned_data = process_file(input_path)
        all_combined.update(cleaned_data)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            for line in cleaned_data:
                f.write(f"{line}\n")
                
        print(f"[+] Kategori '{category}' selesai: {len(cleaned_data)} baris unik -> {output_path}")

    # File Master All-in-One
    master_path = os.path.join(OUTPUT_DIR, "mrk_master_all.txt")
    master_sorted = sorted(list(all_combined), key=len)
    with open(master_path, 'w', encoding='utf-8') as f:
        for line in master_sorted:
            f.write(f"{line}\n")
            
    print(f"[✓] MASTER FILE berhasil dibuat: {len(master_sorted)} total baris -> {master_path}")

if __name__ == "__main__":
    main()
