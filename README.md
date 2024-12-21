<div align="left" style="position: relative;">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>ROADMAP-EXPENSE-TRACKER</h1>
<p align="left">
	<em><code>❯ A simple and efficient command-line expense tracking application built with Python</code></em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/P-Nelly/roadmap-expense-tracker?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/P-Nelly/roadmap-expense-tracker?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/P-Nelly/roadmap-expense-tracker?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/P-Nelly/roadmap-expense-tracker?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="left"><!-- default option, no dependency badges. -->
</p>
<p align="left">
	<!-- default option, no dependency badges. -->
</p>
</div>
<br clear="right">

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

A command-line expense tracking application that helps users manage their personal expenses. The application provides both an interactive menu-driven interface and a command-line interface for adding, updating, deleting, and analyzing expenses. Data is persistently stored in JSON format, making it easy to backup and transfer.

---

##  Features

- **Dual Interface**: Choose between an interactive menu-driven interface or command-line arguments
- **Expense Management**:
  - Add new expenses with descriptions and amounts
  - Update existing expense details
  - Delete unwanted expenses
  - List all expenses in a tabulated format
- **Financial Analysis**:
  - View monthly expense summaries
  - Calculate total expenses
- **Data Persistence**: All expenses are automatically saved to a JSON file
- **Error Handling**: Robust error handling for file operations and user inputs
- **Clean Interface**: Terminal-clearing functionality for better user experience

---

##  Project Structure

```sh
└── roadmap-expense-tracker/
    ├── expenses.json
    └── main.py
```

###  Project Index
<details open>
	<summary><b><code>ROADMAP-EXPENSE-TRACKER/</code></b></summary>
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/P-Nelly/roadmap-expense-tracker/blob/master/main.py'>main.py</a></b></td>
				<td><code>❯ Main application file containing the expense tracker implementation</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/P-Nelly/roadmap-expense-tracker/blob/master/expenses.json'>expenses.json</a></b></td>
				<td><code>❯ JSON file storing the expense data</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with roadmap-expense-tracker, ensure your runtime environment meets the following requirements:

- **Python**: Python 3.6 or higher
- **Dependencies**: tabulate package for table formatting

###  Installation

Install roadmap-expense-tracker using one of the following methods:

**Build from source:**

1. Clone the roadmap-expense-tracker repository:
```sh
❯ git clone https://github.com/P-Nelly/roadmap-expense-tracker
```

2. Navigate to the project directory:
```sh
❯ cd roadmap-expense-tracker
```

3. Install the project dependencies:
```sh
❯ pip install tabulate
```

###  Usage

**Interactive Mode:**
```sh
❯ python main.py
```

**Command Line Interface:**
```sh
# Add an expense
❯ python main.py add --description "Groceries" --amount 50.50

# List all expenses
❯ python main.py list

# Show monthly summary
❯ python main.py summary --month 12

# Delete an expense
❯ python main.py delete --id 1

# Update an expense
❯ python main.py update --id 1 --amount 75.00 --description "Updated description"
```

###  Testing
```sh
❯ python -m unittest discover tests
```

---
##  Project Roadmap

- [X] **`Core Features`**: <strike>Basic expense tracking functionality</strike>
- [X] **`UI Improvements`**: <strike>Interactive menu-driven interface</strike>
- [X] **`Data Management`**: <strike>JSON-based data persistence</strike>
- [ ] **`Data Export`**: Add CSV export functionality
- [ ] **`Categories`**: Add expense categorization
- [ ] **`Data Visualization`**: Add charts and graphs for expense analysis
- [ ] **`Multi-currency Support`**: Add support for different currencies
- [ ] **`Budget Management`**: Add budget setting and tracking

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/P-Nelly/roadmap-expense-tracker/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/P-Nelly/roadmap-expense-tracker/issues)**: Submit bugs found or log feature requests for the `roadmap-expense-tracker` project.
- **💡 [Submit Pull Requests](https://github.com/P-Nelly/roadmap-expense-tracker/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/P-Nelly/roadmap-expense-tracker
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/P-Nelly/roadmap-expense-tracker/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=P-Nelly/roadmap-expense-tracker">
   </a>
</p>
</details>

---

##  License

This project is protected under the [MIT](LICENSE) License. For more details, refer to the [LICENSE](LICENSE) file.

---

##  Acknowledgments

- Thanks to the Python community for the excellent libraries
- Inspired by the need for a simple, efficient expense tracking solution
- Built as part of a learning roadmap project

--- 