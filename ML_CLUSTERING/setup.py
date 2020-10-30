{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "setup.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOjKgdYX68uahbKu8ZNg/rv",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/vineetbiyani09/ML/blob/master/ML_CLUSTERING/setup.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HOYgwggkrzSO"
      },
      "source": [
        "from setuptools import setup\n",
        "\n",
        "with open(\"README.md\", \"r\") as fh:\n",
        "    long_description = fh.read()\n",
        "\n",
        "setup(\n",
        "    name=\"raw\",\n",
        "    version=\"0.0.1\",\n",
        "    description=\"Learning setup\",\n",
        "    py_modules=[\"cluster_selection\"],\n",
        "    package_dir={\"\": \"src\"},\n",
        "    long_description=long_description,\n",
        "    long_description_content_type=\"text/markdown\",\n",
        "    classifiers=[\n",
        "        \"Programming Language :: Python :: 3\",\n",
        "        \"Programming Language :: Python :: 3.6\",\n",
        "        \"Programming Language :: Python :: 3.7\",\n",
        "        \"License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)\",\n",
        "        \"Operating System :: OS Independent\",\n",
        "    ],\n",
        "    url=\"https://github.com/vineetbiyani09/ML/tree/master/ML_CLUSTERING\",\n",
        "    author=\"Jash Bhatia, Vineet Biyani, Yash Doshi, Sagarika Raje\",\n",
        "    author_email=\"vineetbiyani0@gmail.com\",    \n",
        "    install_requires = [\n",
        "        \"blessings ~= 1.7\",\n",
        "    ],\n",
        "\n",
        "    extras_require = {\n",
        "        \"dev\": [\n",
        "            \"pytest >= 3.7\",\n",
        "            \"check-manifest\",\n",
        "            \"twine\",\n",
        "        ],\n",
        "    },\n",
        ")"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}