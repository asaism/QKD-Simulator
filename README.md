# QKD-Simulator

QKD-Simulator is a Python project that simulates the basic concepts of Quantum Key Distribution (QKD). This project uses the Qiskit library to simulate quantum circuits and implements a simplified version of the BB84 protocol.

## Overview

Quantum Key Distribution (QKD) is a method of sharing cryptographic keys between two parties using principles of quantum mechanics. This simulator mimics the main steps of QKD:

1. Generation and transmission of quantum bits by Alice
2. Measurement of quantum bits by Bob
3. Basis reconciliation and key extraction
4. Sampling for eavesdropping detection

## Requirements

- Python 3.7 or higher
- Qiskit
- NumPy

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/asaism/QKD-Simulator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd QKD-Simulator
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the main simulation, use the following command:

```bash
python qkd_simulation.py
```

This script simulates the QKD protocol between Alice and Bob, and displays the generated keys and sampled bits.

## Program Structure

The `qkd_simulation.py` file contains the following main functions:

- `encode_message()`: Alice generates quantum circuits based on bits and bases.
- `measure_message()`: Bob measures the received quantum states.
- `remove_garbage()`: Removes bits measured with mismatched bases.
- `sample_bits()`: Samples bits for eavesdropping detection.

The main execution part uses these functions to simulate each step of the QKD protocol.

## Limitations

This simulator is designed for educational purposes and does not use actual quantum hardware. It is not a full implementation of the BB84 protocol and does not include advanced features such as error correction or privacy amplification.

## Contributing

Contributions to the project are welcome. Please use the GitHub issue tracker for bug reports, feature requests, or pull requests.

## Troubleshooting

### Deprecation Warning for `execute()` function

If you encounter a deprecation warning related to the `execute()` function, the code has been updated to use the latest recommended methods from Qiskit. The current version of the script uses `transpile()` and `simulator.run()` instead of `execute()`, which aligns with Qiskit's future directions.

If you're using an older version of the script, you can update it to the latest version in this repository to resolve the warning.

## License

This project is released under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, please reach out through the [issues](https://github.com/asaism/QKD-Simulator/issues) section of this repository.

---

## QKD-Simulator(in Japanese)

QKD-Simulatorは、量子鍵配布（Quantum Key Distribution, QKD）の基本的な概念をシミュレートするPythonプロジェクトです。このプロジェクトは、Qiskitライブラリを使用して量子回路をシミュレートし、BB84プロトコルの簡略版を実装しています。

## 概要

量子鍵配布（QKD）は、量子力学の原理を利用して、理論上絶対に安全な暗号鍵を2つの当事者間で共有する方法です。このシミュレータは、以下のQKDの主要なステップを模倣します：

1. Aliceによる量子ビットの生成と送信
2. Bobによる量子ビットの測定
3. 基底の照合と鍵の抽出
4. 盗聴検出のためのサンプリング

## 必要条件

- Python 3.7以上
- Qiskit
- NumPy

## インストール

1. このリポジトリをクローンします：

   ```bash
   git clone https://github.com/asaism/QKD-Simulator.git
   ```

2. プロジェクトディレクトリに移動します：

   ```bash
   cd QKD-Simulator
   ```

3. 必要なパッケージをインストールします：

   ```bash
   pip install qiskit numpy
   ```

## 使用方法

メインのシミュレーションを実行するには、以下のコマンドを使用します：

```bash
python qkd_simulation.py
```

このスクリプトは、AliceとBobの間でQKDプロトコルをシミュレートし、生成された鍵とサンプリングされたビットを表示します。

## プログラムの構造

`qkd_simulation.py`ファイルには以下の主要な関数が含まれています：

- `encode_message()`: Aliceがビットと基底に基づいて量子回路を生成します。
- `measure_message()`: Bobが受信した量子状態を測定します。
- `remove_garbage()`: 一致しない基底で測定されたビットを除去します。
- `sample_bits()`: 盗聴検出のためにビットをサンプリングします。

メインの実行部分では、これらの関数を使用してQKDプロトコルの各ステップをシミュレートします。

## 制限事項

このシミュレータは教育目的で設計されており、実際の量子ハードウェアは使用していません。また、完全なBB84プロトコルの実装ではなく、エラー訂正やプライバシー増幅などの高度な機能は含まれていません。

## 貢献

プロジェクトへの貢献を歓迎します。バグ報告、機能リクエスト、プルリクエストなどはGitHubの課題トラッカーを使用してください。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。

## 連絡先

質問や提案がある場合は、[issues](https://github.com/asaism/QKD-Simulator/issues)セクションを通じてお問い合わせください。
