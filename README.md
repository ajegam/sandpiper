Sandpiper

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg .tg-s6z2{text-align:center}
.tg .tg-yw4l{vertical-align:top}
</style>
<table class="tg">
  <tr>
    <th class="tg-s6z2">API</th>
    <th class="tg-s6z2">Notes</th>
    <th class="tg-s6z2">What is Missing?</th>
  </tr>
  <tr>
    <td class="tg-031e">POST Ticket</td>
    <td class="tg-031e">We set all our tickets to the "Normal" status after migration.We did not care to preserve the "Created By" user during the migration.<br>We let it default to the user whose name was used to login during the migration</td>
    <td class="tg-031e">The API did not have<br>- Created Date</td>
  </tr>
  <tr>
    <td class="tg-031e">POST SetTicketStatus</td>
    <td class="tg-031e">Used to set the status of a ticket to New or Closed</td>
    <td class="tg-031e"></td>
  </tr>
  <tr>
    <td class="tg-031e">POST SetAssignee</td>
    <td class="tg-031e">Who the ticket is assigned to.</td>
    <td class="tg-031e"></td>
  </tr>
  <tr>
    <td class="tg-yw4l">POST Comment</td>
    <td class="tg-yw4l">The API does not support passing comment "created by" and "created date". So wetook each comment from JIRA and then added the commented by user at the beginningof each comment.</td>
    <td class="tg-yw4l">The API did not have<br>- Created Date<br>- Comment By</td>
  </tr>
  <tr>
    <td class="tg-yw4l">POST Authorization</td>
    <td class="tg-yw4l">This Post can be used to check if the authorization parameters are correct</td>
    <td class="tg-yw4l"></td>
  </tr>
  <tr>
    <td class="tg-yw4l">POST AttachFile</td>
    <td class="tg-yw4l">The program first downloads all the attachments from JIRA, saves them in a directory and theseimages are then uploaded into JitBit.<br> JIRA can have multiple images with the same name. We were notsure if JitBit can do the same. <br>So the program creates unique image names if duplicates are found byprefixing duplicates with a unique number.</td>
    <td class="tg-yw4l"></td>
  </tr>
  <tr>
    <td class="tg-yw4l">GET UserByEmail</td>
    <td class="tg-yw4l">This API is used to get a user's JitBit id from the Email address. <br>This will be required when you are creating and assigningtickets to different user.</td>
    <td class="tg-yw4l"></td>
  </tr>
</table>

