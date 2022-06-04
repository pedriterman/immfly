# immfly
Technical Interview for Immfly

In this soultion, I used the **django REST framework** to create an API that returns a collection of channels and contents in JSON format.

The model **channel** has a foreign key htat references a different instance of the model. This is done in order to get parent-chil relationship.
Inside this model there are 2 methods:

  **get_all_children**: This method returns all the parent's children, including himself.
  
  **rating_mean**: This method return the mean of the rating of all the contents that are inside this channel, including subchannels. This used the get_all_children method in order to calculate the mean.

The **Content** model defines what a content is. In this scenario, I opted to use a field to save the path of the content, so there is no need to send the full file through the API. In order to save differents kind of metadata, I used a JSONfield to store it. In order to be able to use this with sqlite, I had to enable JSON1 in my windows computer.
  
  In the views.py file there are different views that get a certain query and serializes it in order to send it to the API endpoint
  
  There are differents API endpoints depending on what you want to filter. For example, you can filter content by rating greater than a number.
  
