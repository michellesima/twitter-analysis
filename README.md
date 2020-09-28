# Paraphrasing and ROC Story data

## Paraphrasing data(under `para` folder)
`csv` file columns
| Column        | Meaning       |
| ------------- |:-------------|
| orisen      | original sentence |
| oridel      | original sentence masking out the verbs in the agency category|
| oricat | agency category of the original sentence|
| oriverbs | verbs to be deleted from the original sentence |
| parasen | paraphrase of the original sentence |
| paradel | paraphrase sentence masking out the verbs in the agency category |
| paracat | agency category of the paraphrase sentence|
| paraverbs | verbs to be deleted from the paraphrase sentence |

## ROC Story data(under `roc` folder)
`csv` file columns
| Column | Meaning |
| ------- | :-------|
| sen | original sentence in story |
| sendel | sentence masking out the verbs in the agency category|
| oricat | agency category of the sentence |
| verbs | verbs to be deleted from the sentence |
| storyid | the storyid for the story the sentence is in |
| sentencenum | the sequence number for the sentence in the story |
