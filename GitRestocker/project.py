import sys
import os

class git:

    def init(self, name, language):
        os.system("git init " + name)
        print("Initialized Git repository in " + name)
        os.system("cd " + name)
        os.system("mkdir src && cd src")

        with open("README.md", "w") as f:
            f.write(f'# Template ReStock project for {name} project\n')
            f.write(f'This is a template README file for your {name} project.\n')
            f.write(f'This project was made in {language}\n')
            f.write(f'All files for project are found in src/\n\n')
            f.write(f'# How to run this project\n')

            if language == "python":
                f.write(f'Run the command `python3 src/main.py` to run this project\n')
            
            elif language == "typescript":
                f.write(f'Run the command `ts-node src/main.ts` to run this project\n')
            
            elif language == "javascript":
                f.write(f'Run the command `node src/main.js` to run this project\n')
            
            elif language == "cs" or language == "csharp":
                f.write(f'Run the command `dotnet run` to run this project\n')
            
            else:
                f.write(f'Language not supported. Please choose python, typescript, cs / csharp, or javascript.\n')
            
            f.write(f'\n`To compile the project run: ./ReStock.sh {name} {language} --compile`\n')
        
        f.close()

        os.system(f'mv README.md {name} && git add {name}/README.md')

        try:
            if language == "python":
                with open("src/main.py", "w") as f:
                    f.write(f'# This is a template Python file for your ReStock project called {name}\n')
                    f.write('print("Hello, World!")\n')
                f.close()
                
                os.system("git add src/main.py")

            elif language == "typescript":
                with open("src/main.ts", "w") as f:
                    f.write(f'// This is a template TypeScript file for your ReStock project called {name}\n')
                    f.write('console.log("Hello, World!");\n')
                f.close()
                
                os.system("git add src/main.ts")

            elif language == "javascript":
                with open("src/main.js", "w") as f:
                    f.write(f'// This is a template JavaScript file for your ReStock project called {name}\n')
                    f.write('console.log("Hello, World!");\n')
                f.close()

                os.system("git add src/main.js")
            
            elif language == "cs" or language == "csharp":
                # Create a C# console project in src/
                os.system("dotnet new console --output src")
                
                # Optionally, rename Program.cs to main.cs for consistency
                program_cs = os.path.join("src", "Program.cs")
                main_cs = os.path.join("src", "main.cs")

                if os.path.exists(program_cs):
                    os.rename(program_cs, main_cs)
                
                os.system("git add src/main.cs")

            else:
                print("Language not supported. Please choose python, typescript, cs / csharp, or javascript.")
                return
            
            os.system("mv src/ " + name)
            
        except Exception as e:
            print(f"Error creating main file: {e}")
            return