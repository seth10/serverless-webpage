This repository documents my following the [Build A Serverless Webpage](https://acloud.guru/course/aws-certified-developer-associate/learn/s3/8e263b11-78d2-5971-6e90-81a1e21f3846/watch) lesson from the ACloud.guru course [Certified Developer - Associate 2017](https://acloud.guru/course/aws-certified-developer-associate/dashboard). The purpose of this repository is to document my progress (this will end up taking longer to type than I spent making it), and to throw some shade 😎

I watched the video, then recreated this (mostly) on my own. The way I approached some things differ, but fundamentally the architecture is the same. I didn't like how Ryan was using Lambda to return a static string. My idea was to decorate your name. This would also let me test passing a parameter to the lambda function. For example, if you input `Lancelot`, it might return `Lancelot the Brave`.

First step was to create this function in AWS Lambda.


https://cww70o73r5.execute-api.us-east-1.amazonaws.com/prod/decorateName?name=Seth

http://say-hello.s3-website-us-east-1.amazonaws.com/

https://s3.amazonaws.com/say-hello/index.html

http://say-hello.ficbot.com/


"list of positive adjectives"

https://www.vocabulary.com/lists/238935

Array.prototype.map.call(document.getElementsByClassName("word"), a=>a.innerText)
