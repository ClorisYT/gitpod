from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# 設定資料夾路徑
data_folder = "/workspace/gitpod/data"

@app.route('/api/download/<filename>')
def download_file(filename):
    # 構建文件的完整路徑
    file_path = os.path.join(data_folder, filename)
    
    # 檢查文件是否存在，如果存在就返回
    if os.path.isfile(file_path):
        return send_from_directory(data_folder, filename, as_attachment=True)
    else:
        return "File not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8060, debug=True, use_reloader=True)


