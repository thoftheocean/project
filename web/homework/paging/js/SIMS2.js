function paging()
{
	var sims=document.getElementById('SIMS')
	var rows_count= sims.rows.length;
	var page_count;//总页数
	var psize=5;
    var page_size = psize;//每页显示行数
    var page_index=1;
    
    //总共分多少页
    if(rows_count/page_size > parseInt(rows_count/page_size))
    {
            page_count=parseInt(rows_count/page_size)+1;   
    }else
    {
           page_count=parseInt(rows_count/page_size);   
    } 
  
    //计算开始显示的开始行和结束行
    var startRow = (page_index - 1) * page_size+1;//开始显示的行  
    var endRow = page_index * page_size;//结束显示的行   
        endRow = (endRow > rows_count)? rows_count : endRow;   
        
    //遍历，显示每页的行数
     for(var i=1;i<=rows_count;i++)
     {
         var irow = sims.rows[i-1];
        if(i>=startRow && i<=endRow){
            irow.style.display = "block";    
        }else{
            irow.style.display = "none";
        }
      } 
      
      
    //首页
	var homepage=document.getElementById('homepage')
	homepage.onclick=function(){
	page_index=1;
	var startRow = (page_index - 1) * page_size+1;//开始显示的行  
	var endRow = page_index * page_size;//结束显示的行   
    endRow = (endRow > rows_count)? rows_count : endRow;   
        
    //遍历，显示每页的行数
     for(var i=1;i<=rows_count;i++)
     {
         var irow = sims.rows[i-1];
        if(i>=startRow && i<=endRow){
            irow.style.display = "block";    
        }else{
            irow.style.display = "none";
        }
      } 
		
   	}
	 //上页	
	var pageup=document.getElementById('pageup')
	pageup.onclick=function(){
		if(page_index>1)
		{
			page_index-=1;
		}
		
		var startRow = (page_index - 1) * page_size+1;//开始显示的行  
    	var endRow = page_index * page_size;//结束显示的行   
        endRow = (endRow > rows_count)? rows_count : endRow;   
        
    //遍历，显示每页的行数
	     for(var i=1;i<=rows_count;i++)
	     {
	         var irow = sims.rows[i-1];
	        if(i>=startRow && i<=endRow){
	            irow.style.display = "block";    
	        }else{
	            irow.style.display = "none";
	        } 
	      } 
	
	} 
	//下页	
	var pagedown=document.getElementById('pagedown')
	pagedown.onclick=function(){
		if(page_index<page_count)
		{
			page_index+=1;
		}
		
		 var startRow = (page_index - 1) * page_size+1;//开始显示的行  
        var endRow = page_index * page_size;//结束显示的行   
        endRow = (endRow > rows_count)? rows_count : endRow;   
        
    //遍历，显示每页的行数
     for(var i=1;i<=rows_count;i++)
     {
         var irow = sims.rows[i-1];
        if(i>=startRow && i<=endRow){
            irow.style.display = "block";    
        }else{
            irow.style.display = "none";
        }
      } 
     
	}
	//尾页	
	var endpage=document.getElementById('endpage')
	endpage.onclick=function(){
		
		page_index=page_count;
		var startRow = (page_index - 1) * page_size+1;//开始显示的行  
    	var endRow = page_index * page_size;//结束显示的行   
        endRow = (endRow > rows_count)? rows_count : endRow;   
        
    //遍历，显示每页的行数
     for(var i=1;i<=rows_count;i++)
     {
         var irow = sims.rows[i-1];
        if(i>=startRow && i<=endRow){
            irow.style.display = "block";    
        }else{
            irow.style.display = "none";
        }
      } 
		
	}
	alert(page_index)
	 var tempStr = "共"+rows_count+"条记录 分"+page_count+"页 第"+ page_index +"页";
	 document.getElementById("barcon").innerHTML = tempStr;
	  
	}
	