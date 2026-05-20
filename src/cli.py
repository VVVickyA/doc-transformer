"""
DocTransformer CLI - 命令行工具
"""

import click
from pathlib import Path

from .converter import docx_to_markdown, markdown_to_docx, batch_convert
from .formatter import format_docx, apply_template


@click.group()
@click.version_option(version='0.1.0', prog_name='DocTransformer')
def cli():
    """DocTransformer - 文档转换工具

    让 AI Agent 能够直接识别、编辑 Word/PDF 文档。
    """
    pass


@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('-o', '--output', help='输出文件路径')
def convert(input_file, output):
    """将 Word 文档转换为 Markdown

    示例: dt convert paper.docx
    """
    try:
        result = docx_to_markdown(input_file, output)
        click.echo(f"\n转换完成！可以在 Claude Code 中编辑: {result}")
    except Exception as e:
        click.echo(f"错误: {e}", err=True)
        raise SystemExit(1)


@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('-t', '--template', help='使用模板（如 thesis_cn、thesis_en、resume）')
@click.option('-o', '--output', help='输出文件路径')
def export(input_file, template, output):
    """将 Markdown 转换为 Word 文档

    示例: dt export paper.md --template thesis_cn
    """
    try:
        result = markdown_to_docx(input_file, template, output)
        click.echo(f"\n导出完成！Word 文档: {result}")
    except Exception as e:
        click.echo(f"错误: {e}", err=True)
        raise SystemExit(1)


@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--font', help='正文字体（如 宋体、Times New Roman）')
@click.option('--size', help='正文字号（如 小四、12）')
@click.option('--color', help='正文颜色（如 red、blue、#FF0000）')
@click.option('--heading-font', help='标题字体')
@click.option('--heading-size', help='标题字号')
@click.option('--heading-color', help='标题颜色（如 red、blue、#FF0000）')
@click.option('--line-spacing', type=float, help='行距（如 1.5）')
@click.option('--margin-top', help='上边距（如 2.54cm）')
@click.option('--margin-bottom', help='下边距（如 2.54cm）')
@click.option('--margin-left', help='左边距（如 3.17cm）')
@click.option('--margin-right', help='右边距（如 3.17cm）')
@click.option('--alignment', type=click.Choice(['left', 'center', 'right', 'justify']), help='对齐方式')
@click.option('--first-line-indent', help='首行缩进（如 2cm）')
@click.option('-t', '--template', help='使用模板（如 thesis_cn、thesis_en、resume）')
@click.option('-o', '--output', help='输出文件路径')
def format(input_file, font, size, color, heading_font, heading_size, heading_color,
           line_spacing, margin_top, margin_bottom, margin_left, margin_right,
           alignment, first_line_indent, template, output):
    """修改 Word 文档格式

    示例:

    \b
    # 修改字体和字号
    dt format paper.docx --font "宋体" --size 12

    \b
    # 修改标题颜色
    dt format paper.docx --heading-font "楷体" --heading-size 18 --heading-color blue

    \b
    # 使用模板
    dt format paper.docx --template thesis_cn

    \b
    # 组合修改
    dt format paper.docx --font "楷体" --size 14 --heading-font "楷体" --heading-size 18 --heading-color blue --line-spacing 1.5
    """
    try:
        if template:
            result = apply_template(input_file, template, output)
        else:
            # 构建选项字典
            options = {}
            if font:
                options['font'] = font
            if size:
                options['size'] = size
            if color:
                options['color'] = color
            if heading_font:
                options['heading_font'] = heading_font
            if heading_size:
                options['heading_size'] = heading_size
            if heading_color:
                options['heading_color'] = heading_color
            if line_spacing:
                options['line_spacing'] = line_spacing
            if margin_top:
                options['margin_top'] = margin_top
            if margin_bottom:
                options['margin_bottom'] = margin_bottom
            if margin_left:
                options['margin_left'] = margin_left
            if margin_right:
                options['margin_right'] = margin_right
            if alignment:
                options['alignment'] = alignment
            if first_line_indent:
                options['first_line_indent'] = first_line_indent

            if not options:
                click.echo("错误: 请指定格式选项或使用 --template", err=True)
                raise SystemExit(1)

            result = format_docx(input_file, options, output)

        click.echo(f"\n格式修改完成！文档: {result}")
    except Exception as e:
        click.echo(f"错误: {e}", err=True)
        raise SystemExit(1)


@cli.command()
@click.argument('input_pattern')
@click.option('-f', '--format', 'to_format', type=click.Choice(['md', 'docx']), default='md',
              help='目标格式（md 或 docx）')
@click.option('-o', '--output-dir', help='输出目录')
def batch(input_pattern, to_format, output_dir):
    """批量转换文档

    示例: dt batch "./docs/*.docx" -f md
    """
    try:
        batch_convert(input_pattern, output_dir, to_format)
    except Exception as e:
        click.echo(f"错误: {e}", err=True)
        raise SystemExit(1)


@cli.command()
def templates():
    """列出可用模板

    示例: dt templates
    """
    template_list = [
        ('thesis_cn', '中文论文模板', '宋体，小四，1.5倍行距，上下2.54cm，左右3.17cm'),
        ('thesis_en', '英文论文模板', 'Times New Roman，12pt，2.0倍行距'),
        ('resume', '简历模板', '微软雅黑，小四，1.25倍行距'),
    ]

    click.echo("\n可用模板:")
    click.echo("-" * 60)
    for name, desc, style in template_list:
        click.echo(f"  {name:12} - {desc}")
        click.echo(f"  {'':12}   {style}")
    click.echo("-" * 60)
    click.echo("\n使用方法: dt format paper.docx --template thesis_cn")


if __name__ == '__main__':
    cli()
