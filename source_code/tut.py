import pandas as pd

# open the data file
components_data = pd.read_csv('./data/test_components.csv')
speeches_data = pd.read_csv('./data/test_speeches.csv')

components_data_context = components_data.drop(['Current_Sentence', 'Previous_Sentence', 'Next_Sentence'], axis=1)
# add columns for contexts
components_data_context['Context1'] = ''
components_data_context['Context2'] = ''

print(components_data_context.iloc[6])
speeches = speeches_data[speeches_data['Speech'].str.contains(components_data_context.iloc[6].Text)]
print(speeches['Speech'].values[0])
# for index, row in components_data.iterrows():
    # textToFind = row.Text
    # find the speeches that mention the component
    # speeches = speeches_data[speeches_data['Speech'].str.contains(textToFind)]
    
    
    # # find the 3 sentences closest to the component
    # sentences = speeches['Speech'].values[0].split('. ')
    # # get Index of the sentence that contains the component
    # sentenceIndex = [i for i, s in enumerate(sentences) if textToFind in s][0]
    # context1 = ''
    # # if there is less than 3 sentences in the speeches, then the context1 will be the whole speech
    # if len(sentences) < 3:
    #     context1 = speeches['Speech'].values[0]
    # else:
    #     # if the sentence is the first or the second, then the context1 will be the first 3 sentences
    #     if sentenceIndex < 2:
    #         context1 = '. '.join(sentences[:3])
    #     # if the sentence is the last or the second to last, then the context1 will be the last 3 sentences
    #     elif sentenceIndex > len(sentences) - 3:
    #         context1 = '. '.join(sentences[-3:])
    #     # otherwise, the context1 will be the 3 sentences closest to the component
    #     else:
    #         context1 = '. '.join(sentences[sentenceIndex-1:sentenceIndex+2])
    # # add context1
    # components_data_context.loc[index, 'Context1'] = context1
    # # add full speech to the context2 column
    # components_data_context.loc[index, 'Context2'] = speeches['Speech'].values[0]
    
    
    # I don't believe we should go to a summit con
    
    # Well the conditions I laid out in one of our previous television debates, and it's rather difficult to be much more specific than that. Uh - First of all, we have to have adequate preparation for a summit conference. This means at the secretary of state level and at the ambassadorial level. By adequate preparation I mean that at that level we must prepare an agenda, an agenda agreed upon with the approval of the heads of state involved. Now this agenda should delineate those issues on which there is a possibility of some agreement or negotiation. I don't believe we should go to a summit conference unless we have such an agenda, unless we have some reasonable insur- assurance from Mr. Khrushchev that he intends seriously to negotiate on those points. Now this may seem like a rigid, inflexible position. But let's look at the other side of the coin. If we build up the hopes of the world by having a summit conference that is not adequately prepared, and then, if Mr. Khrushchev finds some excuse for breaking it up - as he did this one - because he isn't going to get his way - we'd set back the cause of peace. We do not help it. We can, in other words, negotiate many of these items of difference between us without going to the summit. I think we have to make a greater effort than we have been making at the secretary of state level, at the ambassadorial level, to work out the differences that we have. And so far as the summit conference is concerned, it should only be entered in upon, it should only be agreed upon, if the negotiations have reached the point that we have some reasonable assurance that something is going to come out of it, other than some phony spirit - a spirit of Geneva, or Camp David, or whatever it is. When I say "phony spirit," I mean phony, not because the spirit is not good on our side, but because the Soviet Union simply doesn't intend to carry out what they say. Now, these are the conditions that I can lay out. I cannot be more precise than that, because until we see what Mr. Khrushchev does and what he says uh - we cannot indicate what our plans will be.