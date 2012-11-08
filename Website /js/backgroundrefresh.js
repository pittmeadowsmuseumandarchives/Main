// JavaScript 

<script type="text/javascript">
function attributeSet(elem, attrb, setting)
{
 var elemAttrb = elem.getAttributeNode(attrb);
 if (elemAttrb)
 {
   elemAttrb.value=setting;
 } else {
   elem.setAttribute(attrb, setting);
 }				
}

function randomClass()
{
 var classes = ["pattern1","pattern2","pattern3"]
 var index = Math.floor(Math.random() * classes.length);
 attributeSet(document.getElementById('myBody'),'class',classes[index]);
}
</script>
