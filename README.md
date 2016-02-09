<html>

<head>
<meta http-equiv=Content-Type content="text/html; charset=unicode">
<meta name=Generator content="Microsoft Word 15 (filtered)">
<title>JIRA to JitBit Migration using REST APIs</title>
</head>

<body lang=EN-US link=blue vlink=purple>

<div class=WordSection1>

<h1>JIRA to JitBit Migration using REST APIs</h1>

<p class=MsoNormal><i><span style='font-size:10.0pt'>Feb 7, 2016</span></i></p>

<p>One of the client's I worked with was a startup that was using JIRA for
their internal issue tracking system. After about 1+ years of usage they found that
JIRA turned out to be more expensive and overly complicated for their needs.
They just needed a simple issue tracking (help desk) system. Their end-users
found JIRA to be overly complicated for what they wanted to do.</p>

<p>Towards the end of Jan 2016, they decided to move to another issue tracking
system called &quot;JitBit&quot;. They found JitBit's pricing model to be very
appealing. JitBit is priced based on &quot;agents&quot; and not the actual
number of users logging the tickets. Agents or Technicians are users in the support
team. &nbsp; This gave them a significant savings over JIRA.  In addition, the
users found JitBit’s simple interface easy to use.  </p>

<p>As part of this move to JitBit the client wanted to migrate tickets from
JIRA to JitBit. The client had over 3000+ issues to migrate and we had to do
the migration for several JIRA projects. So we wanted to someway automate this
migration. We wrote a small Python program that did the migration. The rest of
this document describes the process we followed to migrate data from JIRA to
JitBit and also a short description on the Python program.</p>

<h2>Requirements</h2>

<ol start=1 type=1>
 <li class=MsoNormal>Migrate only a select set of issues from JIRA to JitBit.
     These would be selected using a JIRA filter. By changing the JIRA filter
     you can decide what issues get migrated.</li>
 <li class=MsoNormal>The following fields are to be migrated: </li>
 <ol start=1 type=1>
  <li class=MsoNormal>Summary</li>
  <li class=MsoNormal>Body</li>
  <li class=MsoNormal>Priority</li>
  <li class=MsoNormal>Status</li>
  <li class=MsoNormal>Created By&nbsp;→ All set to one fixed user</li>
  <li class=MsoNormal>Assigned To&nbsp;→ All set to one fixed user</li>
  <li class=MsoNormal>Comments&nbsp;</li>
  <li class=MsoNormal>Attachments</li>
 </ol>
 <li class=MsoNormal>Issues from JIRA “Projects” will be migrated to one
     &quot;Category&quot; in JitBit.</li>
 <li class=MsoNormal>Ability to audit migrated issues in JIRA.</li>
 <li class=MsoNormal>Ability to restart migration process.</li>
 <li class=MsoNormal>Ability to run the migration process in stages.</li>
 <li class=MsoNormal>Ability to locate “partially migrated” issues. </li>
</ol>

<h2>&nbsp;Migration Options</h2>

<p>We considered two options to migrate:</p>

<h3 id="JIRAtoJitBitMigrationusingRESTAPIs-Option1(CSV)">Option 1 (CSV)</h3>

<p>JIRA had an option to export issues to a CSV file and JitBit had a CSV
import option. &nbsp;This was probably the simplest way to do the migration.
However, we ran into the following issues:</p>

<ul type=square>
 <li class=MsoNormal>Comments </li>
 <ul type=square>
  <li class=MsoNormal>The list display in JIRA does not display comments. There
      are JIRA plug-ins that can be used to display comments in the search and
      then export them. But this needed additional configuration in JIRA which
      we did not want to do. </li>
 </ul>
 <li class=MsoNormal>Attachments </li>
 <ul type=square>
  <li class=MsoNormal>Not possible using the CSV approach</li>
 </ul>
</ul>

<p>&nbsp;Due to the limitations on both JIRA and JitBit we quickly figured out
that the CSV approach was not going to work for our requirements.&nbsp;</p>

<h3 id="JIRAtoJitBitMigrationusingRESTAPIs-Option2(API)">Option 2 (API)</h3>

<p>Both JIRA and JitBit support REST API's interfaces. &nbsp;We could use these
APIs to migrate the issues from JIRA. &nbsp;So we wrote a simple Python program
that fetches data from JIRA and then pushes them to JitBit.</p>

<h3
id="JIRAtoJitBitMigrationusingRESTAPIs-JitBitAPIsUsed(https://www.jitbit.com/helpdesk/helpdesk-api/)">JitBit
APIs Used (<a href="https://www.jitbit.com/helpdesk/helpdesk-api/">https://www.jitbit.com/helpdesk/helpdesk-api/</a>)</h3>

<div>

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none'>
 <tr>
  <td valign=top style='border:double windowtext 1.5pt;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b>API</b></p>
  </td>
  <td width=707 valign=top style='width:424.2pt;border:double windowtext 1.5pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b>Notes</b></p>
  </td>
  <td width=195 valign=top style='width:117.0pt;border:double windowtext 1.5pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b>What we missed?</b></p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:double windowtext 1.5pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>POST Authorization</p>
  </td>
  <td width=707 valign=top style='width:424.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>This Post can be used to check if the authorization
  parameters are correct</p>
  </td>
  <td width=195 valign=top style='width:117.0pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>&nbsp;</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:double windowtext 1.5pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>POST Ticket</p>
  </td>
  <td width=707 valign=top style='width:424.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>We set all our tickets to the
  &quot;Normal&quot; status after migration.</p>
  <p style='margin:0in;margin-bottom:.0001pt'>We did not care to preserve the
  &quot;Created By&quot; user during the migration. All the issues would show
  the same created by user.</p>
  <p style='margin:0in;margin-bottom:.0001pt'>You can pass a “behalf-of” user
  id to this POST. This can be used to create a ticket on behalf of someone
  else. Although we did not use this feature the code supports this.</p>
  </td>
  <td width=195 valign=top style='width:117.0pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>The API did not have</p>
  <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:.5in;
  margin-bottom:.0001pt;text-indent:-.25in'>-<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span>Created Date</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:double windowtext 1.5pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>POST Comment</p>
  </td>
  <td width=707 valign=top style='width:424.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>The API does not support passing
  comment &quot;created by&quot; and &quot;created date&quot;. So we took each
  comment from JIRA and then added the user name as a prefix to each comment.</p>
  </td>
  <td width=195 valign=top style='width:117.0pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>The API did not have</p>
  <p class=MsoListParagraphCxSpFirst style='text-indent:-.25in'>-<span
  style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span>Created Date</p>
  <p class=MsoListParagraphCxSpLast style='text-indent:-.25in'>-<span
  style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span>Comment By</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:double windowtext 1.5pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>POST AttachFile</p>
  </td>
  <td width=707 valign=top style='width:424.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>The program first downloads all
  the attachments from JIRA, saves them in a directory and these images are
  then uploaded into JitBit. JIRA can have multiple images with the same name.
  We were not sure if JitBit can do the same. So the program creates unique
  image names if duplicates are found by prefixing duplicates with a unique
  number.</p>
  </td>
  <td width=195 valign=top style='width:117.0pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>&nbsp;</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:double windowtext 1.5pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>GET UserByEmail</p>
  </td>
  <td width=707 valign=top style='width:424.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>This API is used to get a user's JitBit id from the Email address. This
  will be required when you are creating and assigning tickets to different
  user.</p>
  </td>
  <td width=195 valign=top style='width:117.0pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>&nbsp;</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:double windowtext 1.5pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>POST SetTicketStatus</p>
  </td>
  <td width=707 valign=top style='width:424.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>Used to set the status of a ticket to New or Closed</p>
  </td>
  <td width=195 valign=top style='width:117.0pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>&nbsp;</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:double windowtext 1.5pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>POST SetAssignee</p>
  </td>
  <td width=707 valign=top style='width:424.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>Who the ticket is assigned to?</p>
  </td>
  <td width=195 valign=top style='width:117.0pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>&nbsp;</p>
  </td>
 </tr>
</table>

</div>

<p>&nbsp;</p>

<h3
id="JIRAtoJitBitMigrationusingRESTAPIs-JIRAAPIsUsed(https://docs.atlassian.com/jira/REST/latest/)">JIRA
APIs Used (<a href="https://docs.atlassian.com/jira/REST/latest/">https://docs.atlassian.com/jira/REST/latest/</a>)</h3>

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none'>
 <tr>
  <td width=390 valign=top style='width:233.75pt;border:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <h3 align=center style='text-align:center'><span style='font-size:12.0pt'>API</span></h3>
  </td>
  <td width=591 valign=top style='width:354.85pt;border:double windowtext 1.5pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <h3 align=center style='text-align:center'><span style='font-size:12.0pt'>Notes</span></h3>
  </td>
 </tr>
 <tr>
  <td width=390 valign=top style='width:233.75pt;border:double windowtext 1.5pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><a
  href="https://docs.atlassian.com/jira/REST/latest/#api/2/filter"><span
  style='color:windowtext;text-decoration:none'>api/2/filter</span></a></p>
  <p class=MsoNormal><a
  href="https://docs.atlassian.com/jira/REST/latest/#api/2/filter"><span
  style='color:windowtext;text-decoration:none'>Get filter</span></a></p>
  <p class=MsoNormal>GET&nbsp;/rest/api/2/filter/{id}</p>
  </td>
  <td width=591 valign=top style='width:354.85pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'><span style='color:black'>We
  created a filter in JIRA that included all the issues that we wanted to
  migrate. We pass that filter's id to this call to get the filter's URL. Here
  is a sample filter in JIRA created using the &quot;Advanced&quot; filter
  feature:</span></p>
  <p style='margin:0in;margin-bottom:.0001pt;orphans: auto;text-align:start;
  widows: 1;-webkit-text-stroke-width: 0px;word-spacing:0px'><span
  style='color:black'>&nbsp;</span></p>
  <p style='margin:0in;margin-bottom:.0001pt;orphans: auto;text-align:start;
  widows: 1;-webkit-text-stroke-width: 0px;word-spacing:0px'><span
  style='font-size:10.0pt;font-family:"Courier New";color:black'>project = AR
  AND (Tags is EMPTY OR Tags != JITBIT_MIGRATION_SUCCESS) ORDER BY key ASC</span></p>
  <p style='margin:0in;margin-bottom:.0001pt;orphans: auto;text-align:start;
  widows: 1;-webkit-text-stroke-width: 0px;word-spacing:0px'><span
  style='color:black'>&nbsp;</span></p>
  <p style='margin:0in;margin-bottom:.0001pt'><span style='color:black'>Note
  the use of Tags field. We set the JIRA Tags field to
  &quot;JITBIT_MIGRATION_SUCCESS&quot; after we migrated the code successfully.
  Adding this in the filter will help you rerun the program if it fails in the
  middle.</span></p>
  <p style='margin:0in;margin-bottom:.0001pt'><span style='color:black'>This
  call will return a URL.</span></p>
  </td>
 </tr>
 <tr>
  <td width=390 valign=top style='width:233.75pt;border:double windowtext 1.5pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <h3><span style='font-size:12.0pt;font-weight:normal'>Filter URL</span></h3>
  </td>
  <td width=591 valign=top style='width:354.85pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <h3><span style='font-size:12.0pt;font-weight:normal'>We use the URL got from
  the call above and then make another call to get all the issues that we are
  going to migrate.  The call to the filter URL had two limitations – 1. It
  returned all the columns and 2. It returned only the first 50 rows. Appending
  the following parameter at the end of the URL fixed these two problems:</span></h3>
  <h3><span style='font-size:10.0pt;font-family:"Courier New";color:black;
  font-weight:normal'>fields=key&amp;maxResults=10000</span></span></h3>
  <h3><span style='font-size:12.0pt;color:black;font-weight:normal'>This call
  will return a list of all the issues that we have to migrate.</span></h3>
  </td>
 </tr>
 <tr>
  <td width=390 valign=top style='width:233.75pt;border:double windowtext 1.5pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><a
  href="https://docs.atlassian.com/jira/REST/latest/#api/2/issue"><span
  style='color:windowtext;text-decoration:none'>api/2/issue</span></a></p>
  <p class=MsoNormal><a
  href="https://docs.atlassian.com/jira/REST/latest/#api/2/issue-getIssue"><span
  style='color:windowtext;text-decoration:none'>Get issue</span></a></p>
  <p class=MsoNormal>GET&nbsp;/rest/api/2/issue/{issueIdOrKey}</p>
  </td>
  <td width=591 valign=top style='width:354.85pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <h3><span style='font-size:12.0pt;color:black;font-weight:normal'>Given an
  issue id this will return a JSON will all the details (issue_info)</span></h3>
  </td>
 </tr>
 <tr>
  <td width=390 valign=top style='width:233.75pt;border:double windowtext 1.5pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <h3><span style='font-size:12.0pt;color:black;font-weight:normal'>Comments</span></span></h3>
  </td>
  <td width=591 valign=top style='width:354.85pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <h3><span style='font-size:12.0pt;color:black;font-weight:normal'>We get all
  the comments by iterating over the issue info object. JitBit API does not
  provide for passing a comment author. So we appended the comment author to
  the beginning of each comment.</span></span></h3>
  </td>
 </tr>
 <tr>
  <td width=390 valign=top style='width:233.75pt;border:double windowtext 1.5pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <h3><span style='font-size:12.0pt;color:black;font-weight:normal'>Attachments</span></span></h3>
  </td>
  <td width=591 valign=top style='width:354.85pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='color:black'>We get all the attachments by
  iterating over the issues info object. We first create a directory with the
  issue &quot;key&quot; as the name.</span></p>
  <p class=MsoNormal><span style='color:black'>We then save all the attachments
  underneath this directory. If there are duplicate file names, they are made
  unique by adding a prefix.</span></p>
  </td>
 </tr>
 <tr>
  <td width=390 valign=top style='width:233.75pt;border:double windowtext 1.5pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <h3 style='margin:0in;margin-bottom:.0001pt'><span style='font-size:12.0pt;
  color:black;font-weight:normal'><a
  href="https://docs.atlassian.com/jira/REST/latest/#api/2/issue"><span
  style='color:black;text-decoration:none'>api/2/issue</span></a></span></h3>
  <h3 style='margin:0in;margin-bottom:.0001pt;orphans: auto;text-align:start;
  widows: 1;-webkit-text-stroke-width: 0px;word-spacing:0px'><span
  style='font-size:12.0pt;color:black;font-weight:normal'><a
  href="https://docs.atlassian.com/jira/REST/latest/#api/2/issue-editIssue"><span
  style='color:black;text-decoration:none'>Edit issue</span></a></span></h3>
  <h3 style='margin:0in;margin-bottom:.0001pt;orphans: auto;text-align:start;
  widows: 1;-webkit-text-stroke-width: 0px;word-spacing:0px'><span
  style='font-size:12.0pt;color:black;font-weight:normal'>PUT&nbsp;/rest/api/2/issue/{issueIdOrKey}</span></h3>
  <h3><span style='font-size:12.0pt;color:black;font-weight:normal'>&nbsp;</span></h3>
  </td>
  <td width=591 valign=top style='width:354.85pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <h3><span style='font-size:12.0pt;color:black;font-weight:normal'>After
  Migrating the issue to JitBit we then mark the &quot;Tag&quot; field in JIRA
  to a specific value (JITBIT_MIGRATION_SUCCESS).  This is required for
  auditing and also for restarting the program from where it last stopped.</span></span></h3>
  </td>
 </tr>
</table>

<p>&nbsp;</p>

<h2 id=JIRAtoJitBitMigrationusingRESTAPIs-SetuponJIRASide>Setup on JIRA Side</h2>

<div>

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none'>
 <tr>
  <td width=209 valign=top style='width:125.1pt;border:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b>Item</b></p>
  </td>
  <td width=585 valign=top style='width:351.0pt;border:double windowtext 1.5pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b>Description</b></p>
  </td>
  <td width=167 valign=top style='width:100.2pt;border:double windowtext 1.5pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p align=center style='text-align:center'><b>Reference in config.yml</b></p>
  </td>
 </tr>
 <tr>
  <td width=209 valign=top style='width:125.1pt;border:double windowtext 1.5pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>JIRA Filter</p>
  </td>
  <td width=585 valign=top style='width:351.0pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>Create filter that has all the issue you want to migrate. See a sample
  below:</p>
  <div>
  <div><pre style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;
  margin-left:0in'
  data-syntaxhighlighter-params="brush: java; gutter: false; theme: Confluence"
  data-theme=Confluence>project = AR AND (Tags is EMPTY OR Tags != JITBIT_MIGRATION_SUCCESS) ORDER BY key ASC</pre></div>
  </div>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>Make sure to include the Tags field in your query. This is required to
  restart the migration if it fails.<br>
  Note down this filter's id from JIRA - When you click on this filter the URL
  will show the filter id.</p>
  </td>
  <td width=167 valign=top style='width:100.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>&nbsp;jira_filter_id</p>
  </td>
 </tr>
 <tr>
  <td width=209 valign=top style='width:125.1pt;border:double windowtext 1.5pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>JIRA User</p>
  </td>
  <td width=585 valign=top style='width:351.0pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>The user account that is used in the program should
  have permissions to edit/modify the issues in JIRA.</p>
  </td>
  <td width=167 valign=top style='width:100.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>&nbsp;N/A</p>
  </td>
 </tr>
 <tr>
  <td width=209 valign=top style='width:125.1pt;border:double windowtext 1.5pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>Editing Closed Issues</p>
  </td>
  <td width=585 valign=top style='width:351.0pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>After each ticket is migrated we set the Tags field in JIRA. So make
  sure the workflow for the projects in your filter allow for editing issues
  after they have been closed. The default JIRA workflow will not allow you to
  edit an issue after it has been closed.&nbsp;So you will have to change this.</p>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>See&nbsp;<a
  href="https://confluence.atlassian.com/jira061/jira-administrators-faq/usage-faq/allow-editing-of-closed-issues">https://confluence.atlassian.com/jira061/jira-administrators-faq/usage-faq/allow-editing-of-closed-issues</a>&nbsp;for
  more help on this.&nbsp;</p>
  </td>
  <td width=167 valign=top style='width:100.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>N/A&nbsp;</p>
  </td>
 </tr>
 <tr>
  <td width=209 valign=top style='width:125.1pt;border:double windowtext 1.5pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>JIRI API URL</p>
  </td>
  <td width=585 valign=top style='width:351.0pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>Note down the JIRA API URL. Example: <a
  href="https://xyz.atlassian.net/rest/api/2">https://xyz.atlassian.net/rest/api/2</a></p>
  </td>
  <td width=167 valign=top style='width:100.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>&nbsp;jira_api_url</p>
  </td>
 </tr>
 <tr>
  <td width=209 valign=top style='width:125.1pt;border:double windowtext 1.5pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>JIRA User and Password</p>
  </td>
  <td width=585 valign=top style='width:351.0pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>Note down the user id and the password of the user
  that will be used to connect to JIRA from the program</p>
  </td>
  <td width=167 valign=top style='width:100.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>jira_user</p>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>jira_pwd</p>
  </td>
 </tr>
 <tr>
  <td width=209 valign=top style='width:125.1pt;border:double windowtext 1.5pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>Directory to store attachments</p>
  </td>
  <td width=585 valign=top style='width:351.0pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>Location where attachments will be stored. Example: D:/users/xyz/projects/sandpiper/attachments</p>
  </td>
  <td width=167 valign=top style='width:100.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>attachment_folder</p>
  </td>
 </tr>
 <tr>
  <td width=209 valign=top style='width:125.1pt;border:double windowtext 1.5pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>Attachments fetch behavior</p>
  </td>
  <td width=585 valign=top style='width:351.0pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>DELETE_REFRESH → Delete all previously obtained images and download a
  refresh copy</p>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>NEW_ONLY → Download attachments only if a directory with the issue's key
  is missing.</p>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>We had a lot of attachments so, we ran the program ahead of time just
  fetching the attachments (DELETE_REFRESH). On the day of go-live we simple
  change this setting to NEW_ONLY. That way attachments were downloaded only
  when they were missing (i.e. for new issues that were created after our download
  run)</p>
  </td>
  <td width=167 valign=top style='width:100.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>fetch_attachments</p>
  </td>
 </tr>
 <tr>
  <td width=209 valign=top style='width:125.1pt;border:double windowtext 1.5pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>JIRA Tag field id</p>
  </td>
  <td width=585 valign=top style='width:351.0pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>The program will updated a field called &quot;Tag&quot; In JIRA. This is a
  custom field that is available in the hosted JIRA deployments. In our
  instance this was referred to as <span style='color:black'>&quot;customfield_10800&quot;.
  Not sure if this changes for each JIRA install.</span></p>
  </td>
  <td width=167 valign=top style='width:100.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>jira_tag_field</p>
  </td>
 </tr>
</table>

</div>

<h2 id=JIRAtoJitBitMigrationusingRESTAPIs-SetuponJitBitSide>Setup on JitBit
Side</h2>

<div>

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none'>
 <tr>
  <td valign=top style='border:double windowtext 1.5pt;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b>Item</b></p>
  </td>
  <td width=534 valign=top style='width:4.45in;border:double windowtext 1.5pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b>Description</b></p>
  </td>
  <td width=272 valign=top style='width:163.2pt;border:double windowtext 1.5pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p align=center style='margin:0in;margin-bottom:.0001pt;text-align:center'><b>Reference
  in</b></p>
  <p align=center style='margin:0in;margin-bottom:.0001pt;text-align:center'><b>config.yml</b></p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:double windowtext 1.5pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>JitBit Category</p>
  </td>
  <td width=534 valign=top style='width:4.45in;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>We moved Projects in JIRA to
  Categories in JitBit.</p>
  <p style='margin:0in;margin-bottom:.0001pt'>We moved all of our projects to
  one particular category in JitBit. Create this category in JitBit and note
  the id of this category</p>
  </td>
  <td width=272 valign=top style='width:163.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>jitbit_migrate_category_id</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:double windowtext 1.5pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>JitBit Category (for</p>
  <p style='margin:0in;margin-bottom:.0001pt'>partially migrated)</p>
  </td>
  <td width=534 valign=top style='width:4.45in;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>If the migration of a particular issue fails part way through – then this
  issues is moved to this category in JitBit. At the end of migration all
  issues in this category can be deleted.</p>
  </td>
  <td width=272 valign=top style='width:163.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>jitbit_delete_category_id</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:double windowtext 1.5pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>JitBit user id</p>
  </td>
  <td width=534 valign=top style='width:4.45in;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>During the migration we assigned
  all the issues to one particular user in JitBit. This email indicates who
  that user is.</p>
  <p style='margin:0in;margin-bottom:.0001pt'>If your need to is to keep the
  users from JIRA to JitBit the same then make sure all users in JIRA exist in
  JitBit as well.</p>
  </td>
  <td width=272 valign=top style='width:163.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>jitbit_default_assign_email</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:double windowtext 1.5pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>JitBit API URL</p>
  </td>
  <td width=534 valign=top style='width:4.45in;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>Note down the JitBit API URL. Example: <a
  href="https://xyz.jitbit.com/helpdesk/api">https://xyz.jitbit.com/helpdesk/api</a></p>
  </td>
  <td width=272 valign=top style='width:163.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>jitbit_api_url</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:double windowtext 1.5pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>JitBit User and Password</p>
  </td>
  <td width=534 valign=top style='width:4.45in;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>Note down the user id and the
  password of the user that will be used to connect to JItBit from the program.</p>
  <p style='margin:0in;margin-bottom:.0001pt'>When creating issues if the
  &quot;behalf_of&quot; user id is not passed then all issues will show the
  &quot;Created as&quot; by this user</p>
  </td>
  <td width=272 valign=top style='width:163.2pt;border-top:none;border-left:
  none;border-bottom:double windowtext 1.5pt;border-right:double windowtext 1.5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>jitbit_user</p>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>jitbit_pwd</p>
  </td>
 </tr>
</table>

</div>

<p>&nbsp;</p>

<h2 id=JIRAtoJitBitMigrationusingRESTAPIs-ProgramNotes>Python Program Notes</h2>

<p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:.5in;
margin-bottom:.0001pt;text-indent:-.25in'>-<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span>A very small Python program was written to perform the migration. &nbsp;The
standard Python &quot;requests&quot; library (<a
href="http://docs.python-requests.org/en/master/">http://docs.python-requests.org/en/master/</a>)
was used to make the API calls. &nbsp;There is other Python libraries as well
(urllib2). &nbsp;We found the “requests” library to be much simpler to use.</p>

<p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:.5in;
margin-bottom:.0001pt;text-indent:-.25in'>-<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span>Python has a very good JIRA library (<a
href="https://pythonhosted.org/jira/">https://pythonhosted.org/jira/</a>).
&nbsp;However, we did not use this. Since our requirements were quite minimal
we opted to use the &quot;requests&quot; library for all our calls.</p>

<p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:.5in;
margin-bottom:.0001pt;text-indent:-.25in'>-<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span>Uses standard Python libraries. No other downloads are required. Has
been tested on Python 2.7.10.</p>

<p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:.5in;
margin-bottom:.0001pt;text-indent:-.25in'>-<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span>Authentication type &quot;basic_auth&quot; is used for both JIRA and
JitBit.</p>

<p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:.5in;
margin-bottom:.0001pt;text-indent:-.25in'>-<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span>To run:</p>

<p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:1.0in;
margin-bottom:.0001pt;text-indent:-.25in'><span style='font-family:"Courier New"'>o<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp; </span></span>Get a copy of
this code (folk or get a copy from GitHut at https://github.com/ajegam/sandpiper)</p>

<p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:1.0in;
margin-bottom:.0001pt;text-indent:-.25in'><span style='font-family:"Courier New"'>o<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp; </span></span>Setup the
config/config.yml file</p>

<p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:1.0in;
margin-bottom:.0001pt;text-indent:-.25in'><span style='font-family:"Courier New"'>o<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp; </span></span>Execute “python
process_data.py”</p>

<p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:1.0in;
margin-bottom:.0001pt;text-indent:-.25in'><span style='font-family:"Courier New"'>o<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp; </span></span>The class
&quot;ProcessData&quot; in process_data.py is the orchestrating class.</p>

<p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:.5in;
margin-bottom:.0001pt;text-indent:-.25in'>-<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span>To test</p>

<p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:1.0in;
margin-bottom:.0001pt;text-indent:-.25in'><span style='font-family:"Courier New"'>o<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp; </span></span>The ProcessData
class has a test_jitbit() that can be used to test if a specific issue is
getting migrated.</p>

<p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:.5in;
margin-bottom:.0001pt;text-indent:-.25in'>-<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span>As with any other code use with caution and test thoroughly before
using.</p>

</div>

</body>

</html>
