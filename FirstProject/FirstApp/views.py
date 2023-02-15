from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request): #view-function
    #ss ----> is html-data/code
	ss='''		
			<center>
				<h2 style="color:Blue;">
					Hello User, Welcome to Django First-Project First-App
				</h2>
				<hr color="brown" size="3" width="95"/>
			</center>
		''';
	
	return HttpResponse(ss);

    

def show(request):
    ss='''
       <!--
    HTML Webpage to display "Welcome-Message" with different Headings 

-->
    <html>
        <head>  
	        <title>*****Welcome-Page*****</title>
		    <style>
		h1{
		        color:Blue;
		}
		h2{     
		        color:Green;
		}
		h3{
		        color:Red;
		}
		h4{
		        color:orange;
		}
		h5{     
		        color:pink;
		}
		h6{
		        color:violet;
		}
		h1,h3,h5{
		        background-color:maroon;
		}	        
		h2,h4,h6{
		        background-color:lightgreen;
		}
		    </style
	    </head>
	    <body>
	        <center>
	            <h1>Welcome To DJANGO HTML Page</h1>
			    <hr color="orange" width="100%"/> 
		        <h2>Welcome To DJANGO HTML Page</h2>
			    <hr color="orange" width="90%"/>
		        <h3>Welcome To DJANGO HTML Page</h3>
			    <hr color="orange" width="80%"/>
		        <h4>Welcome To DJANGO HTML Page</h4>
			    <hr color="orange" width="70%"/>
		        <h5>Welcome To DJANGO HTML Page</h5>
			    <hr color="orange" width="60%"/>
		        <h6>Welcome To DJANGO HTML Page</h6>
			    <hr color="orange" width="50%"/>
		    </center>	
	    </body>
   </html>
    '''
    return HttpResponse(ss);




def hello(request):
    print("hello/ url is requested & hello() is executed");         
    ss='''
    <html>
        <head>
            <title>Hello Webpage</title>
            <style>
                  h1{
                         color:Blue;
                         width:90%
                  }
                  h2{    color:Green;
                         width:80%;
                  }
                  h3{    color:Red;
                         width:70%;
                  }
                  h1,h2,h3{
                         Background-color:Lightpink;
                         Border:2px dashed Grey;
                   }
                    
            </style>
        </head>
        <body>
            <center>
                <h1>Hello User...!!!</h1>
                <hr color='maroon' width='90%'/> 
                <h2>Welcome to DJANGO-APP</h2>
                <hr color='orange' width='70%'/>
                <h3>Have a Nice-Day...</h3>
                <hr color='green' width='50%'/> 
            </center>
        </body>
    </html>
        ''';
    return HttpResponse(ss);  




import time;	
def senddatetime(request):
	print("dtime/ url is requested & senddatetime() is executed");
	ct = time.ctime()
	print("Client Request Date & time on server :: ",ct);
	ss='''
	<html>
		<head>
			<title>Date-time Webpage</title>
			<style>
				h1{
					color:Blue;
					width:90%;
				}
				h2{
					color:Green;
					width:80%;
				}
				h3{
					color:Red;
					width:70%;
				}
				h1,h2,h3{
					background-color:lightgreen;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Welcome to DJango-User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Server-Date & Time :: </h2>
				<hr color='brown' width='70%'/>
				<h3>''',ct,'''</h3>
				<hr color='brown' width='60%'/>
			</center>
		</body>
	</html>
	''';
	return HttpResponse(ss);
    
    
    
def demo(request):   
	print("mulitple-Requests-URLs same respose");
	htmldata='''<center>
		<h1>Welcome Demo User!!!</h1>
		<hr />
		<h2>This is Same-Output for diff-mulitple-Requests-URLs</h2>
		<hr />
		<h3>Have a Great Day...</h3>
		</center>''';
	return HttpResponse(htmldata);


    