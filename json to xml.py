import json as JS 
import xml.etree.ElementTree as ET  
with open("test3.json", "r") as json_file: 

	data = JS.load(json_file); 
	root = ET.Element("quiz") 
	Maths = ET.SubElement(root, "maths") 

	Q1 = ET.SubElement(Maths, "q1") 
	ET.SubElement(Q1, "question").text = data["quiz"]["maths"]["q1"]["question"] 

	ET.SubElement(Q1, "options").text = str(data["quiz"] ["maths"]["q1"]["options"][0]) 
	
	ET.SubElement(Q1, "options").text = str(data["quiz"]["maths"]["q1"]["options"][1])  
											
	ET.SubElement(Q1, "options").text = str(data["quiz"]["maths"]["q1"]["options"][2]) 								 
	
	ET.SubElement(Q1, "options").text = str(data["quiz"]["maths"]["q1"]["options"][3])  
											 
	ET.SubElement(Q1, "answer").text = str(data["quiz"]["maths"]["q1"]["answer"])   
									
	Q2 = ET.SubElement(Maths, "q2") 
	ET.SubElement(Q2, "question").text = data["quiz"]["maths"]["q2"]["question"] 
	
	ET.SubElement(Q2, "options").text = str(data["quiz"]["maths"]["q2"]["options"][0])  
 
	ET.SubElement(Q2, "options").text = str(data["quiz"]["maths"]["q2"]["options"][1])  

	ET.SubElement(Q2, "options").text = str(data["quiz"]["maths"]["q2"]["options"][2]) 
	
	ET.SubElement(Q2, "options").text = str(data["quiz"]["maths"]["q2"]["options"][3])   

	ET.SubElement(Q2, "answer").text = str(data["quiz"]["maths"]["q2"]["answer"])  
							
	tree = ET.ElementTree(root) 

	tree.write("quiz.xml") 
