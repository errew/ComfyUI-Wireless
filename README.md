# ComfyUI Wireless Transmission Nodes

**English** | [中文](#中文)

A clean, lightweight ComfyUI plugin to transmit data wirelessly between nodes using a global key-value store. This helps clean up messy "spaghetti" workflows by removing long connecting wires.

## Features
- **Zero Latency**: Uses internal Python dictionary storage.
- **Strict Typing**: Separate nodes for `Any`, `Image`, and `Latent` to ensure compatibility with ComfyUI's visual cues.
- **Pass-through**: Set nodes pass the value through, allowing linear workflow continuation.

## Nodes Included
1. **Universal**: `Set Wireless (Any)` / `Get Wireless (Any)` - Works with Model, VAE, Clip, Conditioning, etc.
2. **Image**: `Set Wireless (Image)` / `Get Wireless (Image)` - Blue connections.
3. **Latent**: `Set Wireless (Latent)` / `Get Wireless (Latent)` - Orange connections.

## Installation

### Method 1: Git Clone (Recommended)
1. Navigate to your ComfyUI `custom_nodes` directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ComfyUI-Wireless.git
   ```
3. Restart ComfyUI.

### Method 2: Manual Installation
1. Download the ZIP file of this repository.
2. Extract it into your `ComfyUI/custom_nodes/` folder.
3. Ensure the folder is named `ComfyUI-Wireless`.
4. Restart ComfyUI.

## Usage
1. Add a **Set Wireless** node. Connect your data and give it a unique Key (e.g., "main_face").
2. Place a **Get Wireless** node anywhere else in the graph. Enter the same Key ("main_face").
3. Connect the Get node to your next processing step.

---

# 中文 (Chinese)

# ComfyUI 无线传输节点

**中文** | [English](#english)

一个简洁、轻量级的 ComfyUI 插件，用于通过全局键值对在节点之间无线传输数据。通过移除长距离的连线，帮助你清理混乱的“面条式”工作流。

## 特性
- **零延迟**: 使用 Python 内部字典存储，速度极快。
- **严格类型**: 提供 `Any` (通用)、`Image` (图像) 和 `Latent` (潜空间) 的专用节点，完美适配 ComfyUI 的端口颜色系统。
- **透传设计**: Set 节点支持数据透传，不打断原有的线性工作流。

## 包含的节点
1. **通用型**: `Set Wireless (Any)` / `Get Wireless (Any)` - 适用于 Model, VAE, Clip, Conditioning 等所有类型。
2. **图像型**: `Set Wireless (Image)` / `Get Wireless (Image)` - 对应蓝色端口。
3. **潜空间型**: `Set Wireless (Latent)` / `Get Wireless (Latent)` - 对应橙色端口。

## 安装方法

### 方法 1: Git Clone (推荐)
1. 进入你的 ComfyUI `custom_nodes` 目录：
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. 克隆本仓库（请将下方链接替换为实际仓库地址）：
   ```bash
   git clone https://github.com/your-username/ComfyUI-Wireless.git
   ```
3. 重启 ComfyUI。

### 方法 2: 手动安装
1. 下载本仓库的 ZIP 压缩包。
2. 将其解压到 `ComfyUI/custom_nodes/` 目录下。
3. 确保文件夹名称为 `ComfyUI-Wireless`。
4. 重启 ComfyUI。

## 使用说明
1. 添加一个 **Set Wireless** 节点。连接你的数据并给它起一个唯一的 Key（例如 "main_face"）。
2. 在工作流的任何其他位置放置一个 **Get Wireless** 节点。输入相同的 Key ("main_face")。
3. 将 Get 节点连接到你的下一个处理步骤。
