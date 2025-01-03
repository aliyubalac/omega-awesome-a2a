from setuptools import setup, find_packages

setup(
    name="ai-explorer-whisper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai-whisper",
        "streamlit",
        "torch",
        "torchaudio",
        "pytest",
        "numpy",
        "pandas"
    ],
    author="Your Name",
    description="Whisper integration for AI Explorer Interface",
    python_requires=">=3.8",
)

