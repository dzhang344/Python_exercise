def f(a)
{
    return ["${a}"];
}

pipeline
{
    agent any;
    parameters
    {
        choice(name: 'resolution', choices: ['a', 'b'], description: '')
        booleanParam(name: 'debug', defaultValue: true, description: '')
        choice(name: 'theme', choices: f(params.resolution), description: '')
    }
    stages
    {
        stage("echo")
        {
            steps
            {
                echo "${params.resolution}"
                echo "${params.debug}"
            }
        }
    }
}