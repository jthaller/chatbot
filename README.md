A chatbot trained on my facebook messanger data. My approach has changed pretty dramatically over time, and you can see my thought process by checking out my blog posts. Orginally, the chatbot was trained entirely on the corpus of my Facebook messaging data; however, even 10 years worth of training dialog proved too scared to built a rebust model. To improve performance, I'm now exploring transfer learning. In this repository, tensorflow is utilized to train the model of the cornell movie dialog database. I planned on using this as the base model and fine-tuning the parameters using my Facebook messages. I'm using tensorflow so that I'll be able to easily convert it to a javascript file, which I can then host on a github pages website for free. I stopped working on the Movie Dialogs as my training base because I realized the performamce would already be limited compared to state-of-the-art chatbots. I plan, instead, to utilize GPT-2 or GPT-3 (when available) as my base model and fine-tune that with my messaging data.
