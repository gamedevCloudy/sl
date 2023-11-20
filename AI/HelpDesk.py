class HelpDeskExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            'Printer Issues': {
                'Symptoms': ['Paper jam', 'Print quality issues', 'Not printing'],
                'Solutions': ['Check for paper jams', 'Replace ink or toner cartridges', 'Restart the printer'],
            },
            'Network Problems': {
                'Symptoms': ['Cannot connect to the internet', 'Slow internet speed', 'Connection drops'],
                'Solutions': ['Restart the router', 'Check network cables', 'Contact Internet Service Provider (ISP)'],
            },
            'Software Errors': {
                'Symptoms': ['Crashing applications', 'Error messages', 'Slow performance'],
                'Solutions': ['Update software', 'Reinstall software', 'Run antivirus scan'],
            },
            # Add more categories as needed
        }

    def get_categories(self):
        return list(self.knowledge_base.keys())

    def diagnose_issue(self, user_input):
        for category, details in self.knowledge_base.items():
            for symptom in details['Symptoms']:
                if symptom.lower() in user_input.lower():
                    return category, details['Solutions']
        return None, None

# Example usage:
def main():
    help_desk_system = HelpDeskExpertSystem()

    print("Welcome to the Help Desk Expert System!")

    while True:
        print("\nChoose a category to get assistance:")
        categories = help_desk_system.get_categories()
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")

        choice = input("Enter the number of the category (or 'exit' to quit): ")
        if choice.lower() == 'exit':
            print("Exiting the Help Desk Expert System. Goodbye!")
            break

        try:
            choice_index = int(choice) - 1
            selected_category = categories[choice_index]
            print(f"\nDiagnosing issues related to {selected_category}:")
            user_input = input("Describe the symptoms you are experiencing: ")
            category, solutions = help_desk_system.diagnose_issue(user_input)

            if category:
                print(f"\nPossible issue: {category}")
                print("Recommended solutions:")
                for solution in solutions:
                    print(f"- {solution}")
            else:
                print("\nNo matching issue found. Please contact technical support for further assistance.")

        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid number or 'exit' to quit.")

if __name__ == "__main__":
    main()
