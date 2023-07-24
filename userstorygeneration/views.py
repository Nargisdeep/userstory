from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from langchain import PromptTemplate
from langchain.llms import OpenAI
import openai
import os

# Create your views here.
@api_view(['POST'])
def feature_post(request):
    print(request.data)
    openai_api_key ="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" 
    template="""Below is given a Product Idea.
          Your Goal is to 
          -Give proper features for the product
          -Give an array of features with respect to every user.
          -Please use - to indicate every new feature
          -Give 10 features max
          -Don't give heaading features start from the first feature
        
          Below is the Product Idea:
          PRODUCTIDEA:{product_idea}


          YOUR_RESPONSE:
           """
    prompt=PromptTemplate(
    input_variables=["product_idea"],
    template=template
    )
    llm=OpenAI(temperature=0.5,openai_api_key=openai_api_key)
    input_productidea=request.data
    if input_productidea:
        prompt_with_productidea=prompt.format(product_idea=input_productidea)
        formatted_input=llm(prompt_with_productidea)
        print(type(formatted_input))
    return Response({"data":formatted_input})
@api_view(['POST'])
def story_post(request):
    print(request.data['product_idea'])
   
    openai_api_key ="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" 
    template="""Below is given Product Idea and Feature related to product idea
          Your Goal is to 
          -Give proper User Stories for the feature respective to product idea
          -Give User Story with respect to every aspect  for E.g. Developer,User,QA, Admin etc. and give more than two for every aspect of the feature.
          -Please use - to indicate start of a story not end of a story
          -Dont give headings like developer,User,QA ,Admin etc only give user stories.
          Below is the  Feature:
          PROODUCTIDEA={product_idea}
          FEATURE:{feature}
           


          YOUR_RESPONSE:
           """
    prompt=PromptTemplate(
    input_variables=["product_idea","feature"],
    template=template
    )
    llm=OpenAI(temperature=0.5,openai_api_key=openai_api_key)
    input_idea=request.data['product_idea']
    input_feature=request.data['feature_idea']
    if input_feature:
        prompt_with_feature=prompt.format(product_idea=input_idea,feature=input_feature)
        formatted_input=llm(prompt_with_feature)
        print(type(formatted_input))
    return Response({"data":formatted_input})