# Airodev AI Engine

Welcome to the Airodev Project. It is powered by crewAI. The goal is to build an AI engine that would Integrate with our hosting, enabling AI assisted web design. This AI engine should be flexible, ensuring that we can change the LLM provider based on the latest benchmarks, and cost consideration for inputs and outputs. This means it should be able to use Ollama, OpenAI, Gemini or Anthropic's Claude out of the box to execute web design process.

## Installation

Ensure to have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.



## Running the Project

To kickstart this AI agent and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the airodev Crew, assembling the agents and assigning them tasks as defined in the configuration.

Unmodified, will run the create an output file with the output of a research on LLMs in the root folder.

## Understanding Airodev Crew

The airodev is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, such as reasearching, design, code generation, and application workflow, enabling the system to achieve complex objectives.

## Support

For support, questions, or feedback regarding the Airodev

- Reach out to us through our [GitHub repository](https://github.com/vpronok/airodev1)
-  We use CrewAI framework, whose documentation is here: [documentation](https://docs.crewai.com)


Let's create wonders together with the power and simplicity of crewAI.
