## Idea

I've decided to do for my capstone project something that will be very useful for my work.

To give you a little background, I work for a law firm which has this site (research library/suite of tools, similar to Westlaw or Lexis)  that helps the clients to comply with the financial regs. One of the major benefits of this site is that it has a rich content model which is driven by internally developed vocabularies. Given the fact that the US government is very generous in releasing new regs and docs daily even, there are a lot of documents that we need to tag recurrently. 

To make this tagging process more efficient and less time consuming, I want to build a module in Python that would classify documents using already developed tags (supervised technique). I don't plan to build a website or app this time. I just want a solid python module that would do the job on a local machine and produce probability-based suggestions for the lawyers to review and then promote it as a ground truth to improve the algorithm. 


## Pitfalls

I would imagine my biggest pitfall would be to format the output of the algorithm so that it becomes a csv file with the document titles as one column and the terms as other columns, populated by the probability for each term per document. 
