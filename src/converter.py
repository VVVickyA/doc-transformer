"""
文档转换模块 - 使用 Pandoc 实现 Word ↔ Markdown 转换
"""

import os
import subprocess
import shutil
from pathlib import Path


def docx_to_markdown(input_path, output_path=None):
    """
    将 Word 文档转换为 Markdown

    Args:
        input_path: Word 文档路径
        output_path: 输出 Markdown 路径（可选）

    Returns:
        输出文件路径
    """
    input_path = Path(input_path)
    if not input_path.exists():
        raise FileNotFoundError(f"输入文件不存在: {input_path}")

    # 确定输出路径
    if output_path is None:
        output_path = input_path.with_suffix('.md')
    else:
        output_path = Path(output_path)

    # 创建图片目录
    images_dir = output_path.parent / 'images'
    images_dir.mkdir(exist_ok=True)

    # 备份原文件
    backup_path = input_path.with_suffix('.docx.backup')
    shutil.copy2(input_path, backup_path)

    # 使用 Pandoc 转换
    cmd = [
        'pandoc',
        str(input_path),
        '-t', 'gfm',  # GitHub Flavored Markdown
        '--extract-media', str(images_dir),
        '-o', str(output_path)
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✓ 转换成功: {input_path} → {output_path}")
        print(f"✓ 图片已提取到: {images_dir}")
        print(f"✓ 原文件已备份: {backup_path}")
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"✗ 转换失败: {e.stderr}")
        raise


def markdown_to_docx(input_path, template=None, output_path=None):
    """
    将 Markdown 转换为 Word 文档

    Args:
        input_path: Markdown 文件路径
        template: Word 模板路径（可选）
        output_path: 输出 Word 路径（可选）

    Returns:
        输出文件路径
    """
    input_path = Path(input_path)
    if not input_path.exists():
        raise FileNotFoundError(f"输入文件不存在: {input_path}")

    # 确定输出路径
    if output_path is None:
        output_path = input_path.with_suffix('.docx')
    else:
        output_path = Path(output_path)

    # 备份原文件
    backup_path = input_path.with_suffix('.md.backup')
    shutil.copy2(input_path, backup_path)

    # 构建 Pandoc 命令
    cmd = ['pandoc', str(input_path), '-o', str(output_path)]

    # 如果有模板，使用模板
    if template:
        template_path = Path(template)
        if template_path.exists():
            cmd.extend(['--reference-doc', str(template_path)])
        else:
            print(f"⚠ 模板文件不存在: {template}，使用默认格式")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✓ 转换成功: {input_path} → {output_path}")
        print(f"✓ 原文件已备份: {backup_path}")
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"✗ 转换失败: {e.stderr}")
        raise


def batch_convert(input_pattern, output_dir=None, to_format='md'):
    """
    批量转换文档

    Args:
        input_pattern: 输入文件模式（如 './docs/*.docx'）
        output_dir: 输出目录（可选）
        to_format: 目标格式（'md' 或 'docx'）
    """
    from glob import glob

    files = glob(input_pattern)
    if not files:
        print(f"✗ 没有找到匹配的文件: {input_pattern}")
        return

    print(f"找到 {len(files)} 个文件")

    for file_path in files:
        try:
            if to_format == 'md':
                docx_to_markdown(file_path, output_dir)
            elif to_format == 'docx':
                markdown_to_docx(file_path, output_dir)
        except Exception as e:
            print(f"✗ 转换失败 {file_path}: {e}")

    print(f"✓ 批量转换完成")
