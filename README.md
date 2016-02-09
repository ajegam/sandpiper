<html>

<head>
<meta http-equiv=Content-Type content="text/html; charset=unicode">
<meta name=Generator content="Microsoft Word 15 (filtered)">
<title>JIRA to JitBit Migration using REST APIs</title>
<style>
<!--
@media print {
    #main {
        padding-bottom: 1em !important; /* The default padding of 6em is too much for printouts */
    }

    body {
        font-family: Arial, Helvetica, FreeSans, sans-serif;
        font-size: 10pt;
        line-height: 1.2;
    }

    body, #full-height-container, #main, #page, #content, .has-personal-sidebar #content {
        background: #fff !important;
        color: #000 !important;
        border: 0 !important;
        width: 100% !important;
        height: auto !important;
        min-height: auto !important;
        margin: 0 !important;
        padding: 0 !important;
        display: block !important;
    }

    a, a:link, a:visited, a:focus, a:hover, a:active {
        color: #000;
    }

    #content h1,
    #content h2,
    #content h3,
    #content h4,
    #content h5,
    #content h6 {
        font-family: Arial, Helvetica, FreeSans, sans-serif;
        page-break-after: avoid;
    }

    pre {
        font-family: Monaco, "Courier New", monospace;
    }

    #header,
    .aui-header-inner,
    #navigation,
    #sidebar,
    .sidebar,
    #personal-info-sidebar,
    .ia-fixed-sidebar,
    .page-actions,
    .navmenu,
    .ajs-menu-bar,
    .noprint,
    .inline-control-link,
    .inline-control-link a,
    a.show-labels-editor,
    .global-comment-actions,
    .comment-actions,
    .quick-comment-container,
    #addcomment {
        display: none !important;
    }

    /* CONF-28544 cannot print multiple pages in IE */
    #splitter-content {
        position: relative !important;
    }

    .comment .date::before {
        content: none !important; /* remove middot for print view */
    }

    h1.pagetitle img {
        height: auto;
        width: auto;
    }

    .print-only {
        display: block;
    }

    #footer {
        position: relative !important; /* CONF-17506 Place the footer at end of the content */
        margin: 0;
        padding: 0;
        background: none;
        clear: both;
    }

    #poweredby {
        border-top: none;
        background: none;
    }

    #poweredby li.print-only {
        display: list-item;
        font-style: italic;
    }

    #poweredby li.noprint {
        display: none;
    }

    /* no width controls in print */
    .wiki-content .table-wrap,
    .wiki-content p,
    .panel .codeContent,
    .panel .codeContent pre,
    .image-wrap {
        overflow: visible !important;
    }

    /* TODO - should this work? */
    #children-section,
    #comments-section .comment,
    #comments-section .comment .comment-body,
    #comments-section .comment .comment-content,
    #comments-section .comment p {
        page-break-inside: avoid;
    }

    #page-children a {
        text-decoration: none;
    }

    /**
     hide twixies

     the specificity here is a hack because print styles
     are getting loaded before the base styles. */
    #comments-section.pageSection .section-header,
    #comments-section.pageSection .section-title,
    #children-section.pageSection .section-header,
    #children-section.pageSection .section-title,
    .children-show-hide {
        padding-left: 0;
        margin-left: 0;
    }

    .children-show-hide.icon {
        display: none;
    }

    /* personal sidebar */
    .has-personal-sidebar #content {
        margin-right: 0px;
    }

    .has-personal-sidebar #content .pageSection {
        margin-right: 0px;
    }
}

 /* Font Definitions */
 @font-face
	{font-family:Wingdings;
	panose-1:5 0 0 0 0 0 0 0 0 0;}
@font-face
	{font-family:"Cambria Math";
	panose-1:2 4 5 3 5 4 6 3 2 4;}
@font-face
	{font-family:Consolas;
	panose-1:2 11 6 9 2 2 4 3 2 4;}
 /* Style Definitions */
 p.MsoNormal, li.MsoNormal, div.MsoNormal
	{margin:0in;
	margin-bottom:.0001pt;
	font-size:12.0pt;
	font-family:"Times New Roman",serif;}
h1
	{mso-style-link:"Heading 1 Char";
	margin-right:0in;
	margin-left:0in;
	font-size:24.0pt;
	font-family:"Times New Roman",serif;
	font-weight:bold;}
h2
	{mso-style-link:"Heading 2 Char";
	margin-right:0in;
	margin-left:0in;
	font-size:18.0pt;
	font-family:"Times New Roman",serif;
	font-weight:bold;}
h3
	{mso-style-link:"Heading 3 Char";
	margin-right:0in;
	margin-left:0in;
	font-size:13.5pt;
	font-family:"Times New Roman",serif;
	font-weight:bold;}
h4
	{mso-style-link:"Heading 4 Char";
	margin-right:0in;
	margin-left:0in;
	font-size:12.0pt;
	font-family:"Times New Roman",serif;
	font-weight:bold;}
a:link, span.MsoHyperlink
	{color:blue;
	text-decoration:underline;}
a:visited, span.MsoHyperlinkFollowed
	{color:purple;
	text-decoration:underline;}
p
	{margin-right:0in;
	margin-left:0in;
	font-size:12.0pt;
	font-family:"Times New Roman",serif;}
pre
	{mso-style-link:"HTML Preformatted Char";
	margin:0in;
	margin-bottom:.0001pt;
	font-size:10.0pt;
	font-family:"Courier New";}
span.Heading1Char
	{mso-style-name:"Heading 1 Char";
	mso-style-link:"Heading 1";
	font-family:"Calibri Light",sans-serif;
	color:#2E74B5;}
span.Heading2Char
	{mso-style-name:"Heading 2 Char";
	mso-style-link:"Heading 2";
	font-family:"Calibri Light",sans-serif;
	color:#2E74B5;}
span.Heading3Char
	{mso-style-name:"Heading 3 Char";
	mso-style-link:"Heading 3";
	font-family:"Calibri Light",sans-serif;
	color:#1F4D78;}
span.HTMLPreformattedChar
	{mso-style-name:"HTML Preformatted Char";
	mso-style-link:"HTML Preformatted";
	font-family:Consolas;}
span.Heading4Char
	{mso-style-name:"Heading 4 Char";
	mso-style-link:"Heading 4";
	font-family:"Calibri Light",sans-serif;
	color:#2E74B5;
	font-style:italic;}
.MsoChpDefault
	{font-size:10.0pt;}
@page WordSection1
	{size:8.5in 11.0in;
	margin:1.0in 1.0in 1.0in 1.0in;}
div.WordSection1
	{page:WordSection1;}
 /* List Definitions */
 ol
	{margin-bottom:0in;}
ul
	{margin-bottom:0in;}
-->
</style>

</head>

<body lang=EN-US link=blue vlink=purple>

<div class=WordSection1>

<h1>JIRA to JitBit Migration using REST APIs</h1>

<p>One of the client's I worked with a startup that was using JIRA for their
issue tracking system. After about 1+ years of usage they found that JIRA turned
out to be more expensive and also overly complicated for their usage. They just
needed a simple issue tracking (help desk) system. JIRA was probably an
overkill.</p>

<p>Towards the end of Jan 2016, they decided to migrate to another issue
tracking system called &quot;JitBit&quot;. They found JitBit's pricing model to
be very appealing. JitBit is priced based on &quot;agents&quot; and not the
actual number of users logging the tickets. Agents or Technicians are the
support team that is actually providing the support. &nbsp; As they had only a
small team providing the support the cost benefit as compared to JIRA was
significant. &nbsp;They also found JitBit''s UI very intuitive and easy to
use.&nbsp;</p>

<p>We had over 3000+ issues to migrate and we had to do the migration for
several JIRA projects. So we wanted to someone automate this migration. We
wrote a small Python program that did the migration. The rest of this document
describes the process we following to migrate data from JIRA to JitBit and also
a quick description on the Python program.</p>

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
 <li class=MsoNormal>Issues from all of the projects will be migrated to one
     &quot;Category&quot; in JitBit.</li>
 <li class=MsoNormal>Issues that have been created in JitBit but failed to
     migrate fully will be moved to a &quot;Delete&quot; category. Several
     API's were required before an issue from JIRA could be moved to JitBit. In
     very rare occasions the second or third REST call failed. When that happened
     we simple moved that issue to a &quot;Delete&quot; category in
     JitBit.&nbsp;</li>
</ol>

<p>&nbsp;</p>

<h2>Migration Options</h2>

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

<p>&nbsp;Due to the limitations on both JIRA an JitBit we quickly figured out
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
  <td valign=top style='border:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b>API</b></p>
  </td>
  <td width=852 valign=top style='width:511.35pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b>Notes</b></p>
  </td>
  <td width=210 valign=top style='width:1.75in;border:solid windowtext 1.0pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b>What we missed?</b></p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>POST Authorization</p>
  </td>
  <td width=852 valign=top style='width:511.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>This Post can be used to check if the authorization
  parameters are correct</p>
  </td>
  <td width=210 valign=top style='width:1.75in;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>&nbsp;</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>POST Ticket</p>
  </td>
  <td width=852 valign=top style='width:511.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>We set all our tickets to the
  &quot;Normal&quot; status after migration.</p>
  <p style='margin:0in;margin-bottom:.0001pt'>We did not care to preserve the
  &quot;Created By&quot; user during the migration. All the issues would show
  the same created by user.</p>
  <p>&nbsp;</p>
  </td>
  <td width=210 valign=top style='width:1.75in;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>The API did not have</p>
  <ul type=square>
   <li class=MsoNormal>Created Date</li>
  </ul>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>POST Comment</p>
  </td>
  <td width=852 valign=top style='width:511.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>The API does not support passing comment &quot;created by&quot; and
  &quot;created date&quot;. So we took each comment from JIRA and then added
  the user name as a prefix to each comment.</p>
  </td>
  <td width=210 valign=top style='width:1.75in;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>The API did not have</p>
  <ul type=square>
   <li class=MsoNormal>Created Date</li>
   <li class=MsoNormal>Comment By</li>
  </ul>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>POST AttachFile</p>
  </td>
  <td width=852 valign=top style='width:511.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>The program first downloads all
  the attachments from JIRA, saves them in a directory and these images are
  then uploaded into JitBit. JIRA can have multiple images with the same name.
  We were not sure if JitBit can do the same. So the program creates unique
  image names if duplicates are found by prefixing duplicates with a unique
  number.</p>
  </td>
  <td width=210 valign=top style='width:1.75in;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>&nbsp;</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>GET UserByEmail</p>
  </td>
  <td width=852 valign=top style='width:511.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>This API is used to get a user's JitBit id from the Email address. This
  will be required when you are creating and assigning tickets to different
  user.</p>
  </td>
  <td width=210 valign=top style='width:1.75in;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>&nbsp;</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>POST SetTicketStatus</p>
  </td>
  <td width=852 valign=top style='width:511.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>Used to set the status of a ticket to New or Closed</p>
  </td>
  <td width=210 valign=top style='width:1.75in;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>&nbsp;</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>POST SetAssignee</p>
  </td>
  <td width=852 valign=top style='width:511.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>Who the ticket is assigned to?</p>
  </td>
  <td width=210 valign=top style='width:1.75in;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
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

<div>

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none'>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b>API</b></p>
  </td>
  <td width=632 valign=top style='width:378.9pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b>Notes</b></p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><a
  href="https://docs.atlassian.com/jira/REST/latest/#api/2/filter"><span
  style='color:windowtext;text-decoration:none'>api/2/filter</span></a></p>
  <p class=MsoNormal><a
  href="https://docs.atlassian.com/jira/REST/latest/#api/2/filter"><span
  style='color:windowtext;text-decoration:none'>Get filter</span></a></p>
  <p class=MsoNormal>GET&nbsp;/rest/api/2/filter/{id}</p>
  </td>
  <td width=632 valign=top style='width:378.9pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>We created a filter in JIRA that
  included all the issues that we wanted to migrate. We pass that filter's id
  to this call to get the filter's URL. Here is a sample filter in JIRA created
  using the &quot;Advanced&quot; filter feature:</p>
  <p style='margin:0in;margin-bottom:.0001pt'>&nbsp;</p>
  <p style='margin:0in;margin-bottom:.0001pt'><span style='font-size:9.0pt;
  font-family:"Courier New"'>project = AR AND (Tags is EMPTY OR Tags !=
  JITBIT_MIGRATION_SUCCESS) ORDER BY key ASC</span></p>
  <p style='margin:0in;margin-bottom:.0001pt'>&nbsp;</p>
  <p style='margin:0in;margin-bottom:.0001pt'>Note the use of Tags field. We
  set the JIRA Tags field to &quot;JITBIT_MIGRATION_SUCCESS&quot; after we
  migrated the code successfully. Adding this in the filter will help you rerun
  the program if it fails in the middle.</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>&nbsp;Filter URL</p>
  </td>
  <td width=632 valign=top style='width:378.9pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'><pre><span style='font-size:12.0pt;font-family:
  "Times New Roman",serif'>This is the URL obtained from the Get API call above. </span></pre><pre><span
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>We found that although we had limited this filter to two columns in JIRA the REST API returned all of the columns. We added these two parameters at the end of the URL to limit the fields and also to return all of the rows:</span></pre><pre><span
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>&nbsp;</span></pre>
  <p style='margin:0in;margin-bottom:.0001pt'><span style='font-size:10.0pt;
  font-family:"Courier New"'>fields=key&amp;maxResults=10000</span></p>
  <p style='margin:0in;margin-bottom:.0001pt'><span style='font-size:10.0pt;
  font-family:"Courier New"'>&nbsp;</span></p>
  <p style='margin:0in;margin-bottom:.0001pt'>We iterate over all of the rows
  returned by this call.</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <h3 style='margin:0in;margin-bottom:.0001pt'
  id="JIRAtoJitBitMigrationusingRESTAPIs-api/2/issue"><span style='font-size:
  12.0pt;font-weight:normal'><a
  href="https://docs.atlassian.com/jira/REST/latest/#api/2/issue"><span
  style='color:windowtext;text-decoration:none'>api/2/issue</span></a></span></h3>
  <h4 style='margin:0in;margin-bottom:.0001pt'
  id=JIRAtoJitBitMigrationusingRESTAPIs-Getissue><span style='font-weight:normal'><a
  href="https://docs.atlassian.com/jira/REST/latest/#api/2/issue-getIssue"><span
  style='color:windowtext;text-decoration:none'>Get issue</span></a></span></h4>
  <p class=MsoNormal>GET&nbsp;/rest/api/2/issue/{issueIdOrKey}</p>
  </td>
  <td width=632 valign=top style='width:378.9pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>Given an issue id this will return a JSON will all the
  details (issue_info)</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>Comments</p>
  </td>
  <td width=632 valign=top style='width:378.9pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>We get all the comments by
  iterating over all of the comments for a particular issue. JitBit API does
  not provide for passing a comment author. So we appended the comment author
  to the beginning of each comment.</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>Attachments</p>
  </td>
  <td width=632 valign=top style='width:378.9pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>We get all the attachments by
  iterating over all the attachments for a particular issue. We first create a
  directory with the issue &quot;key&quot; as the name.</p>
  <p style='margin:0in;margin-bottom:.0001pt'>We then save all the attachments
  underneath this directory. If there are duplicate file names, they are made
  unique by adding a prefix.</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <h3 style='margin:0in;margin-bottom:.0001pt'
  id="JIRAtoJitBitMigrationusingRESTAPIs-api/2/issue.1"><span style='font-size:
  12.0pt;font-weight:normal'><a
  href="https://docs.atlassian.com/jira/REST/latest/#api/2/issue"><span
  style='color:windowtext;text-decoration:none'>api/2/issue</span></a></span></h3>
  <h3 style='margin:0in;margin-bottom:.0001pt'><span style='font-size:12.0pt;
  font-weight:normal'><a
  href="https://docs.atlassian.com/jira/REST/latest/#api/2/issue-editIssue"><span
  style='color:windowtext;text-decoration:none'>Edit issue</span></a></span></h3>
  <div>
  <h3 style='margin:0in;margin-bottom:.0001pt'><span style='font-size:12.0pt;
  font-weight:normal'>PUT&nbsp;/rest/api/2/issue/{issueIdOrKey}</span> </h3>
  </div>
  </td>
  <td width=632 valign=top style='width:378.9pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>After Migrating the issue to
  JitBit we then mark the &quot;Tag&quot; field in JIRA to a specific value
  (JITBIT_MIGRATION_SUCCESS) This is required for auditing and also for
  restarting the program from where it last stopped.</p>
  </td>
 </tr>
</table>

</div>

<p>&nbsp;</p>

<h2 id=JIRAtoJitBitMigrationusingRESTAPIs-SetuponJIRASide>Setup on JIRA Side</h2>

<div>

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none'>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b>Item</b></p>
  </td>
  <td width=695 valign=top style='width:416.7pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b>Description</b></p>
  </td>
  <td width=243 valign=top style='width:145.85pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p align=center style='text-align:center'><b>Reference inconfig.yml</b></p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>JIRA Filter</p>
  </td>
  <td width=695 valign=top style='width:416.7pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
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
  <td width=243 valign=top style='width:145.85pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>&nbsp;jira_filter_id</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>JIRA User</p>
  </td>
  <td width=695 valign=top style='width:416.7pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>The user account that is used in the program should
  have permissions to edit/modify the issues in JIRA.</p>
  </td>
  <td width=243 valign=top style='width:145.85pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>&nbsp;N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>Editing Closed Issues</p>
  </td>
  <td width=695 valign=top style='width:416.7pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
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
  <td width=243 valign=top style='width:145.85pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>N/A&nbsp;</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>JIRI API URL</p>
  </td>
  <td width=695 valign=top style='width:416.7pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>Note down the JIRA API URL. Example: <a
  href="https://xyz.atlassian.net/rest/api/2">https://xyz.atlassian.net/rest/api/2</a></p>
  </td>
  <td width=243 valign=top style='width:145.85pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>&nbsp;jira_api_url</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>JIRA User and Password</p>
  </td>
  <td width=695 valign=top style='width:416.7pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>Note down the user id and the password of the user
  that will be used to connect to JIRA from the program</p>
  </td>
  <td width=243 valign=top style='width:145.85pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>jira_user</p>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>jira_pwd</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>Directory to store attachments</p>
  </td>
  <td width=695 valign=top style='width:416.7pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>Location where attachments will be stored. Example: D:/users/xyz/projects/sandpiper/attachments</p>
  </td>
  <td width=243 valign=top style='width:145.85pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>attachment_folder</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>Attachments fetch behavior</p>
  </td>
  <td width=695 valign=top style='width:416.7pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
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
  <td width=243 valign=top style='width:145.85pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>fetch_attachments</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>JIRA Tag field id</p>
  </td>
  <td width=695 valign=top style='width:416.7pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>We will  updated a field called &quot;Tag&quot; In JIRA. This is a custom
  field that is available in the hosted JIRA deployments. In our instance this
  was referred to as <span style='color:black'>&quot;customfield_10800&quot;.
  Not sure if this changes for each JIRA install.</span></p>
  </td>
  <td width=243 valign=top style='width:145.85pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
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
  <td valign=top style='border:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b>Item</b></p>
  </td>
  <td width=738 valign=top style='width:442.5pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b>Description</b></p>
  </td>
  <td width=248 valign=top style='width:148.5pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p align=center style='margin:0in;margin-bottom:.0001pt;text-align:center'><b>Reference
  in</b></p>
  <p align=center style='margin:0in;margin-bottom:.0001pt;text-align:center'><b>config.yml</b></p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>JitBit Category</p>
  </td>
  <td width=738 valign=top style='width:442.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>We moved Projects in JIRA to
  Categories in JitBit.</p>
  <p style='margin:0in;margin-bottom:.0001pt'>We moved all of our projects to
  one particular category in JitBit. Create this category in JitBit and note
  the id of this category</p>
  </td>
  <td width=248 valign=top style='width:148.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal>jitbit_migrate_category_id</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>JitBit Category (for</p>
  <p style='margin:0in;margin-bottom:.0001pt'>partially migrated)</p>
  </td>
  <td width=738 valign=top style='width:442.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>If the migration failed then moved the partially moved issues to this
  category.  Create this category as well and note the category id.</p>
  </td>
  <td width=248 valign=top style='width:148.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>jitbit_delete_category_id</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>JitBit user id</p>
  </td>
  <td width=738 valign=top style='width:442.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>We create all our issues in
  JitBit as one user. We also assigned all the issues to this user. Pre-create
  this user in JitBit.</p>
  <p style='margin:0in;margin-bottom:.0001pt'>If for your case you need to
  maintain the user between JIRA and JitBit please create</p>
  <p style='margin:0in;margin-bottom:.0001pt'>all those users in JitBit ahead
  of time</p>
  </td>
  <td width=248 valign=top style='width:148.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>jitbit_default_assign_email</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>JitBit API URL</p>
  </td>
  <td width=738 valign=top style='width:442.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>Note down the JitBit API URL. Example: <a
  href="https://xyz.jitbit.com/helpdesk/api">https://xyz.jitbit.com/helpdesk/api</a></p>
  </td>
  <td width=248 valign=top style='width:148.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
  12.0pt;margin-left:0in'>jitbit_api_url</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid windowtext 1.0pt;border-top:none;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin-top:12.0pt;margin-right:0in;margin-bottom:12.0pt;margin-left:
  0in'>JitBit User and Password</p>
  </td>
  <td width=738 valign=top style='width:442.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p style='margin:0in;margin-bottom:.0001pt'>Note down the user id and the
  password of the user that will be used to connect to JItBit from the program.</p>
  <p style='margin:0in;margin-bottom:.0001pt'>When creating issues if the
  &quot;behalf_of&quot; user id is not passed then all issues will show the
  &quot;Created as&quot; by this user</p>
  </td>
  <td width=248 valign=top style='width:148.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
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

<h2 id=JIRAtoJitBitMigrationusingRESTAPIs-ProgramNotes>Program Notes</h2>

<p style='margin:0in;margin-bottom:.0001pt'>A very small Python program was
written to perform the migration. &nbsp;The standard Python
&quot;requests&quot; library (<a
href="http://docs.python-requests.org/en/master/">http://docs.python-requests.org/en/master/</a>)
was used to make the API calls. &nbsp;There is other Python libraries as well
(urllib2). &nbsp;We found the “requests” library to be much simpler to use.</p>

<p style='margin:0in;margin-bottom:.0001pt'>&nbsp;</p>

<p style='margin:0in;margin-bottom:.0001pt'>Python has a very good JIRA library
(<a href="https://pythonhosted.org/jira/">https://pythonhosted.org/jira/</a>).
&nbsp;However, we did not use this. Since our requirements were quite minimal
we opted to use the &quot;requests&quot; library for all our calls.</p>

<p style='margin:0in;margin-bottom:.0001pt'>&nbsp;</p>

<p style='margin:0in;margin-bottom:.0001pt'>Uses standard Python libraries. No
other downloads are required. Has been tested on Python 2.7.10.</p>

<p style='margin:0in;margin-bottom:.0001pt'>&nbsp;</p>

<p style='margin:0in;margin-bottom:.0001pt'>Authentication type
&quot;basic_auth&quot; is used for both JIRA and JitBit.</p>

<p style='margin:0in;margin-bottom:.0001pt'>&nbsp;</p>

<p style='margin:0in;margin-bottom:.0001pt'>You will first need to open
config/config.yml file and fill in the required parameters. </p>

<p style='margin:0in;margin-bottom:.0001pt'>&nbsp;</p>

<p style='margin:0in;margin-bottom:.0001pt'>The class &quot;ProcessData&quot;
is the orchestrating class.</p>

<p style='margin:0in;margin-bottom:.0001pt'>&nbsp;</p>

<p style='margin:0in;margin-bottom:.0001pt'>The ProcessData class has a
test_jitbit() that can be used to test if a specific issue is getting migrated.</p>

</div>

</body>

</html>
