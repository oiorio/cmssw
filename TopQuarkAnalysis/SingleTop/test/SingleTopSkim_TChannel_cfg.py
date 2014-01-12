


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>cmssw/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py at CMSSW_5_3_X · oiorio/cmssw</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="https://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta property="og:image" content="https://github.global.ssl.fastly.net/images/modules/logos_page/Octocat.png">
    <meta name="hostname" content="github-fe132-cp1-prd.iad.github.net">
    <meta name="ruby" content="ruby 2.1.0p0-github-tcmalloc (60139581e1) [x86_64-linux]">
    <link rel="assets" href="https://github.global.ssl.fastly.net/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035/">
    <link rel="xhr-socket" href="/_sockets" />
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="808D26B1:4B97:2835F6:52D30EBD" name="octolytics-dimension-request_id" /><meta content="5015337" name="octolytics-actor-id" /><meta content="oiorio" name="octolytics-actor-login" /><meta content="e164323074d064683e2237bcf58aa42aff52f159fb84306047d4fa38d23b38ae" name="octolytics-actor-hash" />
    

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="IMVBvqwNAcRPWplHtGW+jw065a99Zb2cPApHpgClibc=" name="csrf-token" />

    <link href="https://github.global.ssl.fastly.net/assets/github-e0318ec03abae32f266109d4e5ecb65a0ec7ab19.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://github.global.ssl.fastly.net/assets/github2-cb9092efb14f24f935f2ceaa5e139d61b58daec1.css" media="all" rel="stylesheet" type="text/css" />
    

    

      <script src="https://github.global.ssl.fastly.net/assets/frameworks-d4d23eefcbed557582cde6209ccd824fb98255d8.js" type="text/javascript"></script>
      <script src="https://github.global.ssl.fastly.net/assets/github-2a93856bd56c545b500393f229515bfcb515f71c.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="b642137d481deb5aea0154fc9e20903f">

        <link data-pjax-transient rel='permalink' href='/oiorio/cmssw/blob/65d33648fc111b1e5a743c69647e73244c724859/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py'>
  <meta property="og:title" content="cmssw"/>
  <meta property="og:type" content="githubog:gitrepository"/>
  <meta property="og:url" content="https://github.com/oiorio/cmssw"/>
  <meta property="og:image" content="https://github.global.ssl.fastly.net/images/gravatars/gravatar-user-420.png"/>
  <meta property="og:site_name" content="GitHub"/>
  <meta property="og:description" content="cmssw - CMS Offline Software"/>

  <meta name="description" content="cmssw - CMS Offline Software" />

  <meta content="5015337" name="octolytics-dimension-user_id" /><meta content="oiorio" name="octolytics-dimension-user_login" /><meta content="11925474" name="octolytics-dimension-repository_id" /><meta content="oiorio/cmssw" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="true" name="octolytics-dimension-repository_is_fork" /><meta content="10969551" name="octolytics-dimension-repository_parent_id" /><meta content="cms-sw/cmssw" name="octolytics-dimension-repository_parent_nwo" /><meta content="10969551" name="octolytics-dimension-repository_network_root_id" /><meta content="cms-sw/cmssw" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/oiorio/cmssw/commits/CMSSW_5_3_X.atom" rel="alternate" title="Recent Commits to cmssw:CMSSW_5_3_X" type="application/atom+xml" />

  </head>


  <body class="logged_in  env-production linux vis-public fork page-blob">
    <div class="wrapper">
      
      
      
      


      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/">
  <span class="mega-octicon octicon-mark-github"></span>
</a>

    
    <a href="/notifications" class="notification-indicator tooltipped downwards" data-gotokey="n" title="You have unread notifications">
        <span class="mail-status unread"></span>
</a>

      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey=" s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    data-username="oiorio"
      data-repo="oiorio/cmssw"
      data-branch="CMSSW_5_3_X"
      data-sha="1250bb246ab3ebc8e847badc0dd0d7c8ec81eaeb"
  >

    <input type="hidden" name="nwo" value="oiorio/cmssw" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
        <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="https://help.github.com">Help</a></li>
        </ul>
      </div>

    


  <ul id="user-links">
    <li>
      <a href="/oiorio" class="name">
        <img height="20" src="https://2.gravatar.com/avatar/2bf345cf93ede198cad8e7b692c8a029?d=https%3A%2F%2Fidenticons.github.com%2Fa58d9383c89da628d9f511365958978d.png&amp;r=x&amp;s=140" width="20" /> oiorio
      </a>
    </li>

      <li class="new-menu dropdown-toggle js-menu-container">
        <a href="#" class="js-menu-target tooltipped downwards" title="Create new…">
          <span class="octicon octicon-plus"></span>
          <span class="dropdown-arrow"></span>
        </a>

        <div class="js-menu-content">
        </div>
      </li>

      <li>
        <a href="/settings/profile" id="account_settings"
          class="tooltipped downwards"
          aria-label="Account settings "
          title="Account settings ">
          <span class="octicon octicon-tools"></span>
        </a>
      </li>
      <li>
        <a class="tooltipped downwards" href="/logout" data-method="post" id="logout" title="Sign out" aria-label="Sign out">
          <span class="octicon octicon-log-out"></span>
        </a>
      </li>

  </ul>

<div class="js-new-dropdown-contents hidden">
  

<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo-create"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-organization"></span> New organization</a>
  </li>



    <li class="section-title">
      <span title="oiorio/cmssw">This repository</span>
    </li>
      <li>
        <a href="/oiorio/cmssw/settings/collaboration"><span class="octicon octicon-person-add"></span> New collaborator</a>
      </li>
</ul>

</div>


    
  </div>
</div>

      

      




          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="IMVBvqwNAcRPWplHtGW+jw065a99Zb2cPApHpgClibc=" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="11925474" />

    <div class="select-menu js-menu-container js-select-menu">
      <a class="social-count js-social-count" href="/oiorio/cmssw/watchers">
        1
      </a>
      <span class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0">
        <span class="js-select-button">
          <span class="octicon octicon-eye-unwatch"></span>
          Unwatch
        </span>
      </span>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content">
          <div class="select-menu-header">
            <span class="select-menu-title">Notification status</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container" role="menu">

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">You only receive notifications for conversations in which you participate or are @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-watch"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">You receive notifications for all conversations in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-unwatch"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">You do not receive any notifications for conversations in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

  <li>
  

  <div class="js-toggler-container js-social-container starring-container ">
    <a href="/oiorio/cmssw/unstar"
      class="minibutton with-count js-toggler-target star-button starred upwards"
      title="Unstar this repository" data-remote="true" data-method="post" rel="nofollow">
      <span class="octicon octicon-star-delete"></span><span class="text">Unstar</span>
    </a>

    <a href="/oiorio/cmssw/star"
      class="minibutton with-count js-toggler-target star-button unstarred upwards"
      title="Star this repository" data-remote="true" data-method="post" rel="nofollow">
      <span class="octicon octicon-star"></span><span class="text">Star</span>
    </a>

      <a class="social-count js-social-count" href="/oiorio/cmssw/stargazers">
        0
      </a>
  </div>

  </li>


        <li>
          <a href="/oiorio/cmssw/fork" class="minibutton with-count js-toggler-target fork-button lighter upwards" title="Fork this repo" rel="nofollow" data-method="post">
            <span class="octicon octicon-git-branch-create"></span><span class="text">Fork</span>
          </a>
          <a href="/oiorio/cmssw/network" class="social-count">485</a>
        </li>


</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo-forked"></span>
          <span class="author">
            <a href="/oiorio" class="url fn" itemprop="url" rel="author"><span itemprop="title">oiorio</span></a>
          </span>
          <span class="repohead-name-divider">/</span>
          <strong><a href="/oiorio/cmssw" class="js-current-repository js-repo-home-link">cmssw</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

            <span class="fork-flag">
              <span class="text">forked from <a href="/cms-sw/cmssw">cms-sw/cmssw</a></span>
            </span>
        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      

      <div class="repository-with-sidebar repo-container  ">

        <div class="repository-sidebar">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped leftwards" title="Code">
        <a href="/oiorio/cmssw/tree/CMSSW_5_3_X" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /oiorio/cmssw/tree/CMSSW_5_3_X">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


      <li class="tooltipped leftwards" title="Pull Requests">
        <a href="/oiorio/cmssw/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /oiorio/cmssw/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


        <li class="tooltipped leftwards" title="Wiki">
          <a href="/oiorio/cmssw/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_wiki /oiorio/cmssw/wiki">
            <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>
    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped leftwards" title="Pulse">
        <a href="/oiorio/cmssw/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /oiorio/cmssw/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Graphs">
        <a href="/oiorio/cmssw/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /oiorio/cmssw/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Network">
        <a href="/oiorio/cmssw/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /oiorio/cmssw/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


      <div class="sunken-menu-separator"></div>
      <ul class="sunken-menu-group">
        <li class="tooltipped leftwards" title="Settings">
          <a href="/oiorio/cmssw/settings"
            class="sunken-menu-item" data-pjax aria-label="Settings">
            <span class="octicon octicon-tools"></span> <span class="full-word">Settings</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </a>
        </li>
      </ul>
  </div>
</div>

            <div class="only-with-full-nav">
              

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=push">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/oiorio/cmssw.git" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/oiorio/cmssw.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=push">
  <h3><strong>SSH</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="git@github.com:oiorio/cmssw.git" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="git@github.com:oiorio/cmssw.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=push">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/oiorio/cmssw" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/oiorio/cmssw" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <span class="octicon help tooltipped upwards" title="Get help on which URL is right for you.">
    <a href="https://help.github.com/articles/which-remote-url-should-i-use">
    <span class="octicon octicon-question"></span>
    </a>
  </span>
</p>



              <a href="/oiorio/cmssw/archive/CMSSW_5_3_X.zip"
                 class="minibutton sidebar-button"
                 title="Download this repository as a zip file"
                 rel="nofollow">
                <span class="octicon octicon-cloud-download"></span>
                Download ZIP
              </a>
            </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:e1e967e8f21e40154f9afb46a34f120c -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/oiorio/cmssw/find/CMSSW_5_3_X" data-pjax data-hotkey="t" class="js-show-file-finder" style="display:none">Show File Finder</a>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="CMSSW_7_0_X"
    data-ref="CMSSW_5_3_X"
    role="button" aria-label="Switch branches or tags" tabindex="0">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">CMSSW_5_3_X</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/blob/CMSSW_4_1_X/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_X"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_X">CMSSW_4_1_X</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/blob/CMSSW_4_4_X/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_X"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_X">CMSSW_4_4_X</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/blob/CMSSW_5_3_X/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X">CMSSW_5_3_X</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/blob/CMSSW_6_1_X_SLHC/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_X_SLHC"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_X_SLHC">CMSSW_6_1_X_SLHC</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/blob/CMSSW_6_2_X/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X">CMSSW_6_2_X</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/blob/CMSSW_7_0_X/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X">CMSSW_7_0_X</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/blob/gh-pages/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="gh-pages"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="gh-pages">gh-pages</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/blob/imported-CVS-HEAD/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="imported-CVS-HEAD"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="imported-CVS-HEAD">imported-CVS-HEAD</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <form accept-charset="UTF-8" action="/oiorio/cmssw/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="IMVBvqwNAcRPWplHtGW+jw065a99Zb2cPApHpgClibc=" /></div>
            <span class="octicon octicon-git-branch-create select-menu-item-icon"></span>
            <div class="select-menu-item-text">
              <h4>Create branch: <span class="js-new-item-name"></span></h4>
              <span class="description">from ‘CMSSW_5_3_X’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="CMSSW_5_3_X" />
            <input type="hidden" name="path" id="path" value="TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py" />
          </form> <!-- /.select-menu-item -->

      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-08-06-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-08-06-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-08-06-0200">CMSSW_7_0_X_2013-08-06-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-08-05-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-08-05-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-08-05-1400">CMSSW_7_0_X_2013-08-05-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-08-05-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-08-05-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-08-05-0200">CMSSW_7_0_X_2013-08-05-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-08-04-1700/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-08-04-1700"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-08-04-1700">CMSSW_7_0_X_2013-08-04-1700</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-08-04-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-08-04-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-08-04-1400">CMSSW_7_0_X_2013-08-04-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-08-04-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-08-04-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-08-04-0200">CMSSW_7_0_X_2013-08-04-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-08-03-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-08-03-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-08-03-1400">CMSSW_7_0_X_2013-08-03-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-08-03-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-08-03-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-08-03-0200">CMSSW_7_0_X_2013-08-03-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-08-02-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-08-02-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-08-02-1400">CMSSW_7_0_X_2013-08-02-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-08-02-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-08-02-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-08-02-0200">CMSSW_7_0_X_2013-08-02-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-08-01-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-08-01-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-08-01-1400">CMSSW_7_0_X_2013-08-01-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-08-01-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-08-01-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-08-01-0200">CMSSW_7_0_X_2013-08-01-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-31-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-31-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-31-1400">CMSSW_7_0_X_2013-07-31-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-31-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-31-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-31-0200">CMSSW_7_0_X_2013-07-31-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-30-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-30-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-30-1400">CMSSW_7_0_X_2013-07-30-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-30-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-30-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-30-0200">CMSSW_7_0_X_2013-07-30-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-29-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-29-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-29-1400">CMSSW_7_0_X_2013-07-29-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-29-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-29-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-29-0200">CMSSW_7_0_X_2013-07-29-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-28-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-28-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-28-1400">CMSSW_7_0_X_2013-07-28-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-28-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-28-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-28-0200">CMSSW_7_0_X_2013-07-28-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-27-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-27-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-27-1400">CMSSW_7_0_X_2013-07-27-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-27-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-27-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-27-0200">CMSSW_7_0_X_2013-07-27-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-26-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-26-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-26-1400">CMSSW_7_0_X_2013-07-26-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-26-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-26-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-26-0200">CMSSW_7_0_X_2013-07-26-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-25-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-25-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-25-1400">CMSSW_7_0_X_2013-07-25-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-25-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-25-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-25-0200">CMSSW_7_0_X_2013-07-25-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-24-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-24-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-24-1400">CMSSW_7_0_X_2013-07-24-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-24-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-24-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-24-0200">CMSSW_7_0_X_2013-07-24-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-23-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-23-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-23-1400">CMSSW_7_0_X_2013-07-23-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-23-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-23-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-23-0200">CMSSW_7_0_X_2013-07-23-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-22-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-22-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-22-1400">CMSSW_7_0_X_2013-07-22-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-22-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-22-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-22-0200">CMSSW_7_0_X_2013-07-22-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-21-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-21-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-21-1400">CMSSW_7_0_X_2013-07-21-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-21-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-21-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-21-0200">CMSSW_7_0_X_2013-07-21-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-20-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-20-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-20-1400">CMSSW_7_0_X_2013-07-20-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-20-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-20-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-20-0200">CMSSW_7_0_X_2013-07-20-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-19-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-19-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-19-1400">CMSSW_7_0_X_2013-07-19-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-19-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-19-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-19-0200">CMSSW_7_0_X_2013-07-19-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-18-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-18-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-18-1400">CMSSW_7_0_X_2013-07-18-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-18-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-18-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-18-0200">CMSSW_7_0_X_2013-07-18-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-17-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-17-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-17-1400">CMSSW_7_0_X_2013-07-17-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-17-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-17-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-17-0200">CMSSW_7_0_X_2013-07-17-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-16-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-16-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-16-1400">CMSSW_7_0_X_2013-07-16-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-16-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-16-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-16-0200">CMSSW_7_0_X_2013-07-16-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-15-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-15-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-15-1400">CMSSW_7_0_X_2013-07-15-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-15-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-15-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-15-0200">CMSSW_7_0_X_2013-07-15-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-14-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-14-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-14-1400">CMSSW_7_0_X_2013-07-14-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-14-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-14-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-14-0200">CMSSW_7_0_X_2013-07-14-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-13-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-13-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-13-1400">CMSSW_7_0_X_2013-07-13-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-13-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-13-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-13-0200">CMSSW_7_0_X_2013-07-13-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-12-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-12-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-12-1400">CMSSW_7_0_X_2013-07-12-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-12-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-12-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-12-0200">CMSSW_7_0_X_2013-07-12-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-11-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-11-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-11-1400">CMSSW_7_0_X_2013-07-11-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-11-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-11-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-11-0200">CMSSW_7_0_X_2013-07-11-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-10-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-10-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-10-1400">CMSSW_7_0_X_2013-07-10-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-10-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-10-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-10-0200">CMSSW_7_0_X_2013-07-10-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-09-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-09-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-09-1400">CMSSW_7_0_X_2013-07-09-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-09-0900/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-09-0900"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-09-0900">CMSSW_7_0_X_2013-07-09-0900</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-09-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-09-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-09-0200">CMSSW_7_0_X_2013-07-09-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-08-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-08-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-08-1400">CMSSW_7_0_X_2013-07-08-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-08-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-08-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-08-0200">CMSSW_7_0_X_2013-07-08-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-07-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-07-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-07-1400">CMSSW_7_0_X_2013-07-07-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-07-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-07-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-07-0200">CMSSW_7_0_X_2013-07-07-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-06-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-06-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-06-1400">CMSSW_7_0_X_2013-07-06-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-06-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-06-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-06-0200">CMSSW_7_0_X_2013-07-06-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-05-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-05-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-05-1400">CMSSW_7_0_X_2013-07-05-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-05-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-05-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-05-0200">CMSSW_7_0_X_2013-07-05-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-04-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-04-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-04-1400">CMSSW_7_0_X_2013-07-04-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-04-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-04-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-04-0200">CMSSW_7_0_X_2013-07-04-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-03-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-03-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-03-1400">CMSSW_7_0_X_2013-07-03-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-03-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-03-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-03-0200">CMSSW_7_0_X_2013-07-03-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-02-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-02-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-02-1400">CMSSW_7_0_X_2013-07-02-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-02-1100/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-02-1100"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-02-1100">CMSSW_7_0_X_2013-07-02-1100</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-07-02-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-07-02-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-07-02-0200">CMSSW_7_0_X_2013-07-02-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_X_2013-06-26-2200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_X_2013-06-26-2200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_X_2013-06-26-2200">CMSSW_7_0_X_2013-06-26-2200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_0_pre1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_0_pre1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_0_pre1">CMSSW_7_0_0_pre1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_7_0_0_pre0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_7_0_0_pre0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_7_0_0_pre0">CMSSW_7_0_0_pre0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-08-06-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-08-06-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-08-06-0200">CMSSW_6_2_X_2013-08-06-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-08-05-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-08-05-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-08-05-1400">CMSSW_6_2_X_2013-08-05-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-08-05-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-08-05-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-08-05-0200">CMSSW_6_2_X_2013-08-05-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-08-04-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-08-04-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-08-04-1400">CMSSW_6_2_X_2013-08-04-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-08-04-1100/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-08-04-1100"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-08-04-1100">CMSSW_6_2_X_2013-08-04-1100</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-08-03-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-08-03-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-08-03-1400">CMSSW_6_2_X_2013-08-03-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-08-03-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-08-03-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-08-03-0200">CMSSW_6_2_X_2013-08-03-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-08-02-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-08-02-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-08-02-1400">CMSSW_6_2_X_2013-08-02-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-08-02-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-08-02-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-08-02-0200">CMSSW_6_2_X_2013-08-02-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-08-01-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-08-01-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-08-01-1400">CMSSW_6_2_X_2013-08-01-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-08-01-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-08-01-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-08-01-0200">CMSSW_6_2_X_2013-08-01-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-31-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-31-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-31-1400">CMSSW_6_2_X_2013-07-31-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-31-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-31-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-31-0200">CMSSW_6_2_X_2013-07-31-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-30-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-30-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-30-1400">CMSSW_6_2_X_2013-07-30-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-30-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-30-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-30-0200">CMSSW_6_2_X_2013-07-30-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-29-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-29-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-29-1400">CMSSW_6_2_X_2013-07-29-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-29-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-29-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-29-0200">CMSSW_6_2_X_2013-07-29-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-28-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-28-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-28-1400">CMSSW_6_2_X_2013-07-28-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-28-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-28-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-28-0200">CMSSW_6_2_X_2013-07-28-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-27-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-27-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-27-1400">CMSSW_6_2_X_2013-07-27-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-27-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-27-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-27-0200">CMSSW_6_2_X_2013-07-27-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-26-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-26-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-26-1400">CMSSW_6_2_X_2013-07-26-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-26-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-26-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-26-0200">CMSSW_6_2_X_2013-07-26-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-25-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-25-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-25-1400">CMSSW_6_2_X_2013-07-25-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-25-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-25-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-25-0200">CMSSW_6_2_X_2013-07-25-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-24-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-24-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-24-1400">CMSSW_6_2_X_2013-07-24-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-24-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-24-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-24-0200">CMSSW_6_2_X_2013-07-24-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-23-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-23-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-23-1400">CMSSW_6_2_X_2013-07-23-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-23-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-23-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-23-0200">CMSSW_6_2_X_2013-07-23-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-22-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-22-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-22-1400">CMSSW_6_2_X_2013-07-22-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-22-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-22-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-22-0200">CMSSW_6_2_X_2013-07-22-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-21-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-21-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-21-1400">CMSSW_6_2_X_2013-07-21-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-21-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-21-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-21-0200">CMSSW_6_2_X_2013-07-21-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-20-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-20-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-20-1400">CMSSW_6_2_X_2013-07-20-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-20-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-20-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-20-0200">CMSSW_6_2_X_2013-07-20-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-19-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-19-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-19-1400">CMSSW_6_2_X_2013-07-19-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-19-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-19-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-19-0200">CMSSW_6_2_X_2013-07-19-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_X_2013-07-18-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_X_2013-07-18-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_X_2013-07-18-1400">CMSSW_6_2_X_2013-07-18-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_0_pre8/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_0_pre8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_0_pre8">CMSSW_6_2_0_pre8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_0_pre7_g496p02/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_0_pre7_g496p02"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_0_pre7_g496p02">CMSSW_6_2_0_pre7_g496p02</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_0_pre7_TS133806/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_0_pre7_TS133806"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_0_pre7_TS133806">CMSSW_6_2_0_pre7_TS133806</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_0_pre7_TS132947/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_0_pre7_TS132947"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_0_pre7_TS132947">CMSSW_6_2_0_pre7_TS132947</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_0_pre7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_0_pre7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_0_pre7">CMSSW_6_2_0_pre7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_0_pre6_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_0_pre6_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_0_pre6_patch1">CMSSW_6_2_0_pre6_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_0_pre6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_0_pre6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_0_pre6">CMSSW_6_2_0_pre6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_0_pre5slc6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_0_pre5slc6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_0_pre5slc6">CMSSW_6_2_0_pre5slc6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_0_pre5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_0_pre5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_0_pre5">CMSSW_6_2_0_pre5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_0_pre4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_0_pre4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_0_pre4">CMSSW_6_2_0_pre4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_0_pre3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_0_pre3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_0_pre3">CMSSW_6_2_0_pre3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_0_pre2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_0_pre2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_0_pre2">CMSSW_6_2_0_pre2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_0_pre1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_0_pre1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_0_pre1">CMSSW_6_2_0_pre1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_0_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_0_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_0_patch1">CMSSW_6_2_0_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_2_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_2_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_2_0">CMSSW_6_2_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_X_SLHC_2013-07-21-1300/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_X_SLHC_2013-07-21-1300"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_X_SLHC_2013-07-21-1300">CMSSW_6_1_X_SLHC_2013-07-21-1300</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_X_SLHC_2013-07-21-0100/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_X_SLHC_2013-07-21-0100"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_X_SLHC_2013-07-21-0100">CMSSW_6_1_X_SLHC_2013-07-21-0100</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_X_SLHC_2013-07-20-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_X_SLHC_2013-07-20-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_X_SLHC_2013-07-20-1400">CMSSW_6_1_X_SLHC_2013-07-20-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_X_2012-12-19-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_X_2012-12-19-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_X_2012-12-19-0200">CMSSW_6_1_X_2012-12-19-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_2_SLHC8/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_2_SLHC8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_2_SLHC8">CMSSW_6_1_2_SLHC8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_2_SLHC7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_2_SLHC7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_2_SLHC7">CMSSW_6_1_2_SLHC7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_2_SLHC6_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_2_SLHC6_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_2_SLHC6_patch1">CMSSW_6_1_2_SLHC6_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_2_SLHC6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_2_SLHC6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_2_SLHC6">CMSSW_6_1_2_SLHC6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_2_SLHC5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_2_SLHC5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_2_SLHC5">CMSSW_6_1_2_SLHC5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_2_SLHC4_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_2_SLHC4_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_2_SLHC4_patch1">CMSSW_6_1_2_SLHC4_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_2_SLHC4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_2_SLHC4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_2_SLHC4">CMSSW_6_1_2_SLHC4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_2_SLHC3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_2_SLHC3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_2_SLHC3">CMSSW_6_1_2_SLHC3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_2_SLHC2_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_2_SLHC2_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_2_SLHC2_patch3">CMSSW_6_1_2_SLHC2_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_2_SLHC2_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_2_SLHC2_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_2_SLHC2_patch2">CMSSW_6_1_2_SLHC2_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_2_SLHC2_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_2_SLHC2_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_2_SLHC2_patch1">CMSSW_6_1_2_SLHC2_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_2_SLHC2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_2_SLHC2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_2_SLHC2">CMSSW_6_1_2_SLHC2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_2_SLHC1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_2_SLHC1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_2_SLHC1">CMSSW_6_1_2_SLHC1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_2">CMSSW_6_1_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_1_SLHCphase2tk1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_1_SLHCphase2tk1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_1_SLHCphase2tk1">CMSSW_6_1_1_SLHCphase2tk1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_1_SLHCphase1tk1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_1_SLHCphase1tk1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_1_SLHCphase1tk1">CMSSW_6_1_1_SLHCphase1tk1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_1">CMSSW_6_1_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_0_pre8/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_0_pre8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_0_pre8">CMSSW_6_1_0_pre8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_0_pre7_TS127013/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_0_pre7_TS127013"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_0_pre7_TS127013">CMSSW_6_1_0_pre7_TS127013</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_0_pre7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_0_pre7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_0_pre7">CMSSW_6_1_0_pre7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_0_pre6g496cand01/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_0_pre6g496cand01"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_0_pre6g496cand01">CMSSW_6_1_0_pre6g496cand01</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_0_pre6_TS126203_TS126341_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_0_pre6_TS126203_TS126341_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_0_pre6_TS126203_TS126341_patch1">CMSSW_6_1_0_pre6_TS126203_TS126341_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_0_pre6_TS126203_TS126341/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_0_pre6_TS126203_TS126341"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_0_pre6_TS126203_TS126341">CMSSW_6_1_0_pre6_TS126203_TS126341</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_0_pre6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_0_pre6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_0_pre6">CMSSW_6_1_0_pre6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_0_pre5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_0_pre5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_0_pre5">CMSSW_6_1_0_pre5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_0_pre4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_0_pre4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_0_pre4">CMSSW_6_1_0_pre4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_0_pre3_TS124729/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_0_pre3_TS124729"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_0_pre3_TS124729">CMSSW_6_1_0_pre3_TS124729</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_0_pre3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_0_pre3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_0_pre3">CMSSW_6_1_0_pre3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_0_pre2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_0_pre2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_0_pre2">CMSSW_6_1_0_pre2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_0_pre1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_0_pre1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_0_pre1">CMSSW_6_1_0_pre1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_1_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_1_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_1_0">CMSSW_6_1_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_X_2012-08-07-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_X_2012-08-07-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_X_2012-08-07-0200">CMSSW_6_0_X_2012-08-07-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_X/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_X"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_X">CMSSW_6_0_X</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_1_PostLS1v2_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_1_PostLS1v2_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_1_PostLS1v2_patch4">CMSSW_6_0_1_PostLS1v2_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_1_PostLS1v2_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_1_PostLS1v2_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_1_PostLS1v2_patch3">CMSSW_6_0_1_PostLS1v2_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_1_PostLS1v2_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_1_PostLS1v2_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_1_PostLS1v2_patch2">CMSSW_6_0_1_PostLS1v2_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_1_PostLS1v2_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_1_PostLS1v2_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_1_PostLS1v2_patch1">CMSSW_6_0_1_PostLS1v2_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_1_PostLS1v2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_1_PostLS1v2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_1_PostLS1v2">CMSSW_6_0_1_PostLS1v2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_1_PostLS1v1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_1_PostLS1v1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_1_PostLS1v1">CMSSW_6_0_1_PostLS1v1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_1">CMSSW_6_0_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_0_pre11/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_0_pre11"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_0_pre11">CMSSW_6_0_0_pre11</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_0_pre10/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_0_pre10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_0_pre10">CMSSW_6_0_0_pre10</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_0_pre9/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_0_pre9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_0_pre9">CMSSW_6_0_0_pre9</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_0_pre8/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_0_pre8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_0_pre8">CMSSW_6_0_0_pre8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_0_pre7py273/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_0_pre7py273"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_0_pre7py273">CMSSW_6_0_0_pre7py273</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_0_pre7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_0_pre7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_0_pre7">CMSSW_6_0_0_pre7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_0_pre6g495p01/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_0_pre6g495p01"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_0_pre6g495p01">CMSSW_6_0_0_pre6g495p01</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_0_pre6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_0_pre6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_0_pre6">CMSSW_6_0_0_pre6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_0_pre5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_0_pre5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_0_pre5">CMSSW_6_0_0_pre5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_0_pre4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_0_pre4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_0_pre4">CMSSW_6_0_0_pre4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_0_pre3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_0_pre3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_0_pre3">CMSSW_6_0_0_pre3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_0_pre2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_0_pre2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_0_pre2">CMSSW_6_0_0_pre2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_0_pre1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_0_pre1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_0_pre1">CMSSW_6_0_0_pre1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_0_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_0_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_0_patch1">CMSSW_6_0_0_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_0_TS123272/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_0_TS123272"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_0_TS123272">CMSSW_6_0_0_TS123272</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_0_SLHCtkpre1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_0_SLHCtkpre1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_0_SLHCtkpre1">CMSSW_6_0_0_SLHCtkpre1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_6_0_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_6_0_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_6_0_0">CMSSW_6_0_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-08-06-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-08-06-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-08-06-0200">CMSSW_5_3_X_2013-08-06-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-08-05-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-08-05-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-08-05-1400">CMSSW_5_3_X_2013-08-05-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-08-05-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-08-05-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-08-05-0200">CMSSW_5_3_X_2013-08-05-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-08-04-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-08-04-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-08-04-1400">CMSSW_5_3_X_2013-08-04-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-08-03-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-08-03-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-08-03-1400">CMSSW_5_3_X_2013-08-03-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-08-03-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-08-03-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-08-03-0200">CMSSW_5_3_X_2013-08-03-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-08-02-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-08-02-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-08-02-1400">CMSSW_5_3_X_2013-08-02-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-08-02-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-08-02-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-08-02-0200">CMSSW_5_3_X_2013-08-02-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-08-01-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-08-01-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-08-01-1400">CMSSW_5_3_X_2013-08-01-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-08-01-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-08-01-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-08-01-0200">CMSSW_5_3_X_2013-08-01-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-31-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-31-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-31-1400">CMSSW_5_3_X_2013-07-31-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-31-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-31-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-31-0200">CMSSW_5_3_X_2013-07-31-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-30-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-30-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-30-1400">CMSSW_5_3_X_2013-07-30-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-30-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-30-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-30-0200">CMSSW_5_3_X_2013-07-30-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-29-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-29-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-29-1400">CMSSW_5_3_X_2013-07-29-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-29-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-29-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-29-0200">CMSSW_5_3_X_2013-07-29-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-28-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-28-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-28-1400">CMSSW_5_3_X_2013-07-28-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-28-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-28-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-28-0200">CMSSW_5_3_X_2013-07-28-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-27-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-27-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-27-1400">CMSSW_5_3_X_2013-07-27-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-27-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-27-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-27-0200">CMSSW_5_3_X_2013-07-27-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-26-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-26-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-26-1400">CMSSW_5_3_X_2013-07-26-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-26-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-26-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-26-0200">CMSSW_5_3_X_2013-07-26-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-25-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-25-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-25-1400">CMSSW_5_3_X_2013-07-25-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-25-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-25-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-25-0200">CMSSW_5_3_X_2013-07-25-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-24-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-24-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-24-1400">CMSSW_5_3_X_2013-07-24-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-24-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-24-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-24-0200">CMSSW_5_3_X_2013-07-24-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-23-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-23-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-23-1400">CMSSW_5_3_X_2013-07-23-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-23-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-23-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-23-0200">CMSSW_5_3_X_2013-07-23-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-22-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-22-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-22-1400">CMSSW_5_3_X_2013-07-22-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-22-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-22-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-22-0200">CMSSW_5_3_X_2013-07-22-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-21-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-21-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-21-1400">CMSSW_5_3_X_2013-07-21-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-21-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-21-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-21-0200">CMSSW_5_3_X_2013-07-21-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-20-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-20-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-20-1400">CMSSW_5_3_X_2013-07-20-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-20-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-20-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-20-0200">CMSSW_5_3_X_2013-07-20-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-19-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-19-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-19-1400">CMSSW_5_3_X_2013-07-19-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-19-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-19-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-19-0200">CMSSW_5_3_X_2013-07-19-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-18-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-18-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-18-1400">CMSSW_5_3_X_2013-07-18-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_X_2013-07-16-1400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_X_2013-07-16-1400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_X_2013-07-16-1400">CMSSW_5_3_X_2013-07-16-1400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_11_sherpa2beta2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_11_sherpa2beta2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_11_sherpa2beta2">CMSSW_5_3_11_sherpa2beta2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_11_patch5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_11_patch5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_11_patch5">CMSSW_5_3_11_patch5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_11_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_11_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_11_patch4">CMSSW_5_3_11_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_11_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_11_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_11_patch3">CMSSW_5_3_11_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_11_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_11_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_11_patch2">CMSSW_5_3_11_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_11_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_11_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_11_patch1">CMSSW_5_3_11_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_11/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_11"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_11">CMSSW_5_3_11</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_10_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_10_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_10_patch2">CMSSW_5_3_10_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_10_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_10_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_10_patch1">CMSSW_5_3_10_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_10/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_10">CMSSW_5_3_10</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_9_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_9_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_9_patch3">CMSSW_5_3_9_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_9_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_9_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_9_patch2">CMSSW_5_3_9_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_9_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_9_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_9_patch1">CMSSW_5_3_9_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_9/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_9">CMSSW_5_3_9</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_8_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_8_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_8_patch3">CMSSW_5_3_8_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_8_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_8_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_8_patch2">CMSSW_5_3_8_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_8_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_8_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_8_patch1">CMSSW_5_3_8_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_8_HI_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_8_HI_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_8_HI_patch2">CMSSW_5_3_8_HI_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_8_HI_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_8_HI_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_8_HI_patch1">CMSSW_5_3_8_HI_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_8_HI/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_8_HI"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_8_HI">CMSSW_5_3_8_HI</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_8/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_8">CMSSW_5_3_8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_7_patch6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_7_patch6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_7_patch6">CMSSW_5_3_7_patch6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_7_patch5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_7_patch5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_7_patch5">CMSSW_5_3_7_patch5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_7_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_7_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_7_patch4">CMSSW_5_3_7_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_7_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_7_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_7_patch3">CMSSW_5_3_7_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_7_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_7_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_7_patch2">CMSSW_5_3_7_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_7_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_7_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_7_patch1">CMSSW_5_3_7_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_7_alcapatch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_7_alcapatch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_7_alcapatch1">CMSSW_5_3_7_alcapatch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_7_25nspatch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_7_25nspatch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_7_25nspatch1">CMSSW_5_3_7_25nspatch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_7">CMSSW_5_3_7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_6_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_6_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_6_patch1">CMSSW_5_3_6_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_5">CMSSW_5_3_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_4_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_4_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_4_patch2">CMSSW_5_3_4_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_4_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_4_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_4_patch1">CMSSW_5_3_4_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_4_cand2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_4_cand2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_4_cand2">CMSSW_5_3_4_cand2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_4_cand1_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_4_cand1_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_4_cand1_patch1">CMSSW_5_3_4_cand1_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_4_cand1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_4_cand1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_4_cand1">CMSSW_5_3_4_cand1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_4_TC125616patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_4_TC125616patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_4_TC125616patch1">CMSSW_5_3_4_TC125616patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_4">CMSSW_5_3_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_3_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_3_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_3_patch3">CMSSW_5_3_3_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_3_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_3_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_3_patch2">CMSSW_5_3_3_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_3_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_3_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_3_patch1">CMSSW_5_3_3_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_3_cand1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_3_cand1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_3_cand1">CMSSW_5_3_3_cand1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_3">CMSSW_5_3_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_2_patch5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_2_patch5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_2_patch5">CMSSW_5_3_2_patch5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_2_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_2_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_2_patch4">CMSSW_5_3_2_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_2_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_2_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_2_patch2">CMSSW_5_3_2_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_2_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_2_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_2_patch1">CMSSW_5_3_2_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_2_metpatch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_2_metpatch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_2_metpatch1">CMSSW_5_3_2_metpatch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_2">CMSSW_5_3_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_1">CMSSW_5_3_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_0_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_0_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_0_patch1">CMSSW_5_3_0_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_3_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_3_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_3_0">CMSSW_5_3_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_X_2012-05-03-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_X_2012-05-03-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_X_2012-05-03-0200">CMSSW_5_2_X_2012-05-03-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_X_2012-03-08-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_X_2012-03-08-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_X_2012-03-08-0200">CMSSW_5_2_X_2012-03-08-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_9/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_9">CMSSW_5_2_9</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_8/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_8">CMSSW_5_2_8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_7_hltpatch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_7_hltpatch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_7_hltpatch2">CMSSW_5_2_7_hltpatch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_7">CMSSW_5_2_7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_6_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_6_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_6_patch2">CMSSW_5_2_6_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_6_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_6_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_6_patch1">CMSSW_5_2_6_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_6_hltpatch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_6_hltpatch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_6_hltpatch1">CMSSW_5_2_6_hltpatch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_6">CMSSW_5_2_6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_5_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_5_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_5_patch3">CMSSW_5_2_5_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_5_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_5_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_5_patch2">CMSSW_5_2_5_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_5_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_5_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_5_patch1">CMSSW_5_2_5_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_5_ecalpatch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_5_ecalpatch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_5_ecalpatch1">CMSSW_5_2_5_ecalpatch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_5_cand1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_5_cand1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_5_cand1">CMSSW_5_2_5_cand1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_5">CMSSW_5_2_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_4_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_4_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_4_patch4">CMSSW_5_2_4_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_4_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_4_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_4_patch3">CMSSW_5_2_4_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_4_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_4_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_4_patch2">CMSSW_5_2_4_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_4_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_4_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_4_patch1">CMSSW_5_2_4_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_4_hltpatch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_4_hltpatch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_4_hltpatch4">CMSSW_5_2_4_hltpatch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_4_hltpatch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_4_hltpatch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_4_hltpatch2">CMSSW_5_2_4_hltpatch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_4">CMSSW_5_2_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_3_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_3_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_3_patch4">CMSSW_5_2_3_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_3_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_3_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_3_patch3">CMSSW_5_2_3_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_3_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_3_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_3_patch2">CMSSW_5_2_3_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_3_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_3_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_3_patch1">CMSSW_5_2_3_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_3">CMSSW_5_2_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_2">CMSSW_5_2_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_1">CMSSW_5_2_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_2_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_2_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_2_0">CMSSW_5_2_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_1_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_1_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_1_3">CMSSW_5_1_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_1_2_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_1_2_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_1_2_patch1">CMSSW_5_1_2_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_1_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_1_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_1_2">CMSSW_5_1_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_1_1_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_1_1_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_1_1_patch3">CMSSW_5_1_1_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_1_1_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_1_1_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_1_1_patch2">CMSSW_5_1_1_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_1_1_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_1_1_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_1_1_patch1">CMSSW_5_1_1_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_1_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_1_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_1_1">CMSSW_5_1_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_0_X_2011-12-18-0200/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_0_X_2011-12-18-0200"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_0_X_2011-12-18-0200">CMSSW_5_0_X_2011-12-18-0200</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_0_1_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_0_1_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_0_1_patch3">CMSSW_5_0_1_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_0_1_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_0_1_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_0_1_patch2">CMSSW_5_0_1_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_0_1_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_0_1_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_0_1_patch1">CMSSW_5_0_1_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_0_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_0_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_0_1">CMSSW_5_0_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_0_0_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_0_0_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_0_0_patch1">CMSSW_5_0_0_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_5_0_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_5_0_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_5_0_0">CMSSW_5_0_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_X_2011-06-09-0400/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_X_2011-06-09-0400"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_X_2011-06-09-0400">CMSSW_4_4_X_2011-06-09-0400</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_5_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_5_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_5_patch4">CMSSW_4_4_5_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_5_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_5_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_5_patch3">CMSSW_4_4_5_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_5_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_5_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_5_patch2">CMSSW_4_4_5_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_5_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_5_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_5_patch1">CMSSW_4_4_5_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_5">CMSSW_4_4_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_4">CMSSW_4_4_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_3_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_3_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_3_patch1">CMSSW_4_4_3_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_3">CMSSW_4_4_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_2_patch10/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_2_patch10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_2_patch10">CMSSW_4_4_2_patch10</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_2_patch9/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_2_patch9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_2_patch9">CMSSW_4_4_2_patch9</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_2_patch8/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_2_patch8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_2_patch8">CMSSW_4_4_2_patch8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_2_patch7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_2_patch7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_2_patch7">CMSSW_4_4_2_patch7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_2_patch6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_2_patch6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_2_patch6">CMSSW_4_4_2_patch6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_2_patch5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_2_patch5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_2_patch5">CMSSW_4_4_2_patch5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_2_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_2_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_2_patch4">CMSSW_4_4_2_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_2_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_2_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_2_patch3">CMSSW_4_4_2_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_2_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_2_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_2_patch2">CMSSW_4_4_2_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_2_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_2_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_2_patch1">CMSSW_4_4_2_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_2">CMSSW_4_4_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_1">CMSSW_4_4_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_0_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_0_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_0_patch4">CMSSW_4_4_0_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_0_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_0_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_0_patch3">CMSSW_4_4_0_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_0_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_0_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_0_patch2">CMSSW_4_4_0_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_0_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_0_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_0_patch1">CMSSW_4_4_0_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_4_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_4_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_4_0">CMSSW_4_4_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_3_0_dqmpatch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_3_0_dqmpatch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_3_0_dqmpatch2">CMSSW_4_3_0_dqmpatch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_3_0_dqmpatch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_3_0_dqmpatch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_3_0_dqmpatch1">CMSSW_4_3_0_dqmpatch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_3_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_3_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_3_0">CMSSW_4_3_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_9_HLT3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_9_HLT3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_9_HLT3">CMSSW_4_2_9_HLT3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_9_HLT2_hltpatch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_9_HLT2_hltpatch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_9_HLT2_hltpatch1">CMSSW_4_2_9_HLT2_hltpatch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_9_HLT2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_9_HLT2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_9_HLT2">CMSSW_4_2_9_HLT2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_9_HLT1_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_9_HLT1_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_9_HLT1_patch1">CMSSW_4_2_9_HLT1_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_9_HLT1_hltpatch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_9_HLT1_hltpatch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_9_HLT1_hltpatch2">CMSSW_4_2_9_HLT1_hltpatch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_9_HLT1_bphpatch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_9_HLT1_bphpatch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_9_HLT1_bphpatch4">CMSSW_4_2_9_HLT1_bphpatch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_9_HLT1_bphpatch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_9_HLT1_bphpatch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_9_HLT1_bphpatch3">CMSSW_4_2_9_HLT1_bphpatch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_9_HLT1_bphpatch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_9_HLT1_bphpatch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_9_HLT1_bphpatch2">CMSSW_4_2_9_HLT1_bphpatch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_9_HLT1_bphpatch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_9_HLT1_bphpatch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_9_HLT1_bphpatch1">CMSSW_4_2_9_HLT1_bphpatch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_9_HLT1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_9_HLT1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_9_HLT1">CMSSW_4_2_9_HLT1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_9_HLT/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_9_HLT"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_9_HLT">CMSSW_4_2_9_HLT</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_patch7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_patch7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_patch7">CMSSW_4_2_8_patch7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_patch6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_patch6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_patch6">CMSSW_4_2_8_patch6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_patch5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_patch5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_patch5">CMSSW_4_2_8_patch5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_patch4">CMSSW_4_2_8_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_patch3">CMSSW_4_2_8_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_patch2">CMSSW_4_2_8_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_patch1">CMSSW_4_2_8_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_p7rootfix/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_p7rootfix"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_p7rootfix">CMSSW_4_2_8_p7rootfix</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHCtk_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHCtk_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHCtk_patch2">CMSSW_4_2_8_SLHCtk_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHCtk_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHCtk_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHCtk_patch1">CMSSW_4_2_8_SLHCtk_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHCtk3_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHCtk3_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHCtk3_patch2">CMSSW_4_2_8_SLHCtk3_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHCtk3_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHCtk3_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHCtk3_patch1">CMSSW_4_2_8_SLHCtk3_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHCtk3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHCtk3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHCtk3">CMSSW_4_2_8_SLHCtk3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHCtk2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHCtk2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHCtk2">CMSSW_4_2_8_SLHCtk2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHCtk/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHCtk"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHCtk">CMSSW_4_2_8_SLHCtk</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHCstd2_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHCstd2_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHCstd2_patch2">CMSSW_4_2_8_SLHCstd2_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHCstd2_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHCstd2_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHCstd2_patch1">CMSSW_4_2_8_SLHCstd2_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHCstd2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHCstd2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHCstd2">CMSSW_4_2_8_SLHCstd2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHCstd/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHCstd"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHCstd">CMSSW_4_2_8_SLHCstd</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHChcal6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHChcal6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHChcal6">CMSSW_4_2_8_SLHChcal6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHChcal5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHChcal5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHChcal5">CMSSW_4_2_8_SLHChcal5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHChcal4_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHChcal4_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHChcal4_patch4">CMSSW_4_2_8_SLHChcal4_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHChcal4_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHChcal4_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHChcal4_patch3">CMSSW_4_2_8_SLHChcal4_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHChcal4_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHChcal4_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHChcal4_patch2">CMSSW_4_2_8_SLHChcal4_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHChcal4_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHChcal4_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHChcal4_patch1">CMSSW_4_2_8_SLHChcal4_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHChcal4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHChcal4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHChcal4">CMSSW_4_2_8_SLHChcal4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHChcal3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHChcal3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHChcal3">CMSSW_4_2_8_SLHChcal3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHChcal2_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHChcal2_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHChcal2_patch3">CMSSW_4_2_8_SLHChcal2_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHChcal2_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHChcal2_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHChcal2_patch2">CMSSW_4_2_8_SLHChcal2_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHChcal2_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHChcal2_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHChcal2_patch1">CMSSW_4_2_8_SLHChcal2_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHChcal/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHChcal"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHChcal">CMSSW_4_2_8_SLHChcal</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHC2_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHC2_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHC2_patch2">CMSSW_4_2_8_SLHC2_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHC2_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHC2_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHC2_patch1">CMSSW_4_2_8_SLHC2_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHC2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHC2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHC2">CMSSW_4_2_8_SLHC2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8_SLHC1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8_SLHC1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8_SLHC1">CMSSW_4_2_8_SLHC1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_8/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_8">CMSSW_4_2_8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_7_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_7_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_7_patch2">CMSSW_4_2_7_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_7_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_7_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_7_patch1">CMSSW_4_2_7_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_7_hltpatch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_7_hltpatch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_7_hltpatch3">CMSSW_4_2_7_hltpatch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_7_hltpatch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_7_hltpatch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_7_hltpatch2">CMSSW_4_2_7_hltpatch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_7_hltpatch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_7_hltpatch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_7_hltpatch1">CMSSW_4_2_7_hltpatch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_7">CMSSW_4_2_7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_6">CMSSW_4_2_6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_5_hltpatch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_5_hltpatch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_5_hltpatch1">CMSSW_4_2_5_hltpatch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_5">CMSSW_4_2_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_4_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_4_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_4_patch2">CMSSW_4_2_4_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_4_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_4_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_4_patch1">CMSSW_4_2_4_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_4_hltpatch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_4_hltpatch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_4_hltpatch1">CMSSW_4_2_4_hltpatch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_4">CMSSW_4_2_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_3_patch5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_3_patch5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_3_patch5">CMSSW_4_2_3_patch5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_3_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_3_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_3_patch4">CMSSW_4_2_3_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_3_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_3_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_3_patch3">CMSSW_4_2_3_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_3_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_3_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_3_patch2">CMSSW_4_2_3_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_3_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_3_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_3_patch1">CMSSW_4_2_3_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_3_SLHC4_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_3_SLHC4_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_3_SLHC4_patch1">CMSSW_4_2_3_SLHC4_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_3_SLHC4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_3_SLHC4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_3_SLHC4">CMSSW_4_2_3_SLHC4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_3_SLHC3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_3_SLHC3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_3_SLHC3">CMSSW_4_2_3_SLHC3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_3_SLHC2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_3_SLHC2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_3_SLHC2">CMSSW_4_2_3_SLHC2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_3">CMSSW_4_2_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_2_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_2_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_2_patch2">CMSSW_4_2_2_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_2_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_2_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_2_patch1">CMSSW_4_2_2_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_2">CMSSW_4_2_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_1_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_1_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_1_patch2">CMSSW_4_2_1_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_1_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_1_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_1_patch1">CMSSW_4_2_1_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_1">CMSSW_4_2_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_2_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_2_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_2_0">CMSSW_4_2_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_8_patch13/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_8_patch13"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_8_patch13">CMSSW_4_1_8_patch13</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_8_patch11/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_8_patch11"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_8_patch11">CMSSW_4_1_8_patch11</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_8_patch10/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_8_patch10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_8_patch10">CMSSW_4_1_8_patch10</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_8_patch8/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_8_patch8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_8_patch8">CMSSW_4_1_8_patch8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_8_patch7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_8_patch7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_8_patch7">CMSSW_4_1_8_patch7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_8_patch6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_8_patch6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_8_patch6">CMSSW_4_1_8_patch6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_8_patch5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_8_patch5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_8_patch5">CMSSW_4_1_8_patch5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_8_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_8_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_8_patch4">CMSSW_4_1_8_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_8_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_8_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_8_patch1">CMSSW_4_1_8_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_8/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_8">CMSSW_4_1_8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_7_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_7_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_7_patch3">CMSSW_4_1_7_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_7_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_7_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_7_patch2">CMSSW_4_1_7_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_7_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_7_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_7_patch1">CMSSW_4_1_7_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_7">CMSSW_4_1_7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_6_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_6_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_6_patch1">CMSSW_4_1_6_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_6">CMSSW_4_1_6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_5">CMSSW_4_1_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_4_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_4_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_4_patch4">CMSSW_4_1_4_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_4_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_4_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_4_patch3">CMSSW_4_1_4_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_4_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_4_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_4_patch2">CMSSW_4_1_4_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_4_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_4_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_4_patch1">CMSSW_4_1_4_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_4">CMSSW_4_1_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_3_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_3_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_3_patch2">CMSSW_4_1_3_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_3">CMSSW_4_1_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_2_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_2_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_2_patch1">CMSSW_4_1_2_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_4_1_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_4_1_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_4_1_2">CMSSW_4_1_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_11_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_11_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_11_3">CMSSW_3_11_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_11_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_11_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_11_2">CMSSW_3_11_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_11_1_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_11_1_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_11_1_patch3">CMSSW_3_11_1_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_11_1_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_11_1_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_11_1_patch2">CMSSW_3_11_1_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_11_1_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_11_1_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_11_1_patch1">CMSSW_3_11_1_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_11_1_hltpatch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_11_1_hltpatch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_11_1_hltpatch1">CMSSW_3_11_1_hltpatch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_11_1_hclpatch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_11_1_hclpatch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_11_1_hclpatch1">CMSSW_3_11_1_hclpatch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_11_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_11_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_11_1">CMSSW_3_11_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_11_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_11_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_11_0">CMSSW_3_11_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_10_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_10_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_10_1">CMSSW_3_10_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_10_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_10_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_10_0">CMSSW_3_10_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_9_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_9_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_9_patch1">CMSSW_3_9_9_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_9/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_9">CMSSW_3_9_9</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_8_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_8_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_8_patch2">CMSSW_3_9_8_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_8_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_8_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_8_patch1">CMSSW_3_9_8_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_8/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_8">CMSSW_3_9_8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_7">CMSSW_3_9_7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_6">CMSSW_3_9_6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_5_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_5_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_5_patch2">CMSSW_3_9_5_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_5_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_5_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_5_patch1">CMSSW_3_9_5_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_5">CMSSW_3_9_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_4">CMSSW_3_9_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_3">CMSSW_3_9_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_2_patch5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_2_patch5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_2_patch5">CMSSW_3_9_2_patch5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_2_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_2_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_2_patch4">CMSSW_3_9_2_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_2_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_2_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_2_patch3">CMSSW_3_9_2_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_2_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_2_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_2_patch2">CMSSW_3_9_2_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_2_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_2_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_2_patch1">CMSSW_3_9_2_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_2">CMSSW_3_9_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_1_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_1_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_1_patch1">CMSSW_3_9_1_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_1">CMSSW_3_9_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_9_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_9_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_9_0">CMSSW_3_9_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_7_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_7_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_7_patch1">CMSSW_3_8_7_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_7">CMSSW_3_8_7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_6_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_6_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_6_patch1">CMSSW_3_8_6_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_6">CMSSW_3_8_6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_5_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_5_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_5_patch3">CMSSW_3_8_5_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_5_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_5_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_5_patch2">CMSSW_3_8_5_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_5_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_5_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_5_patch1">CMSSW_3_8_5_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_5">CMSSW_3_8_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_4_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_4_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_4_patch4">CMSSW_3_8_4_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_4_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_4_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_4_patch3">CMSSW_3_8_4_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_4_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_4_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_4_patch2">CMSSW_3_8_4_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_4_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_4_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_4_patch1">CMSSW_3_8_4_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_4">CMSSW_3_8_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_3">CMSSW_3_8_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_2_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_2_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_2_patch1">CMSSW_3_8_2_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_2">CMSSW_3_8_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_1_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_1_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_1_patch4">CMSSW_3_8_1_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_1_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_1_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_1_patch3">CMSSW_3_8_1_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_1_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_1_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_1_patch2">CMSSW_3_8_1_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_1_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_1_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_1_patch1">CMSSW_3_8_1_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_1">CMSSW_3_8_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_0_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_0_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_0_patch1">CMSSW_3_8_0_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_8_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_8_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_8_0">CMSSW_3_8_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_7_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_7_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_7_1">CMSSW_3_7_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_7_0_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_7_0_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_7_0_patch4">CMSSW_3_7_0_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_7_0_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_7_0_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_7_0_patch3">CMSSW_3_7_0_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_7_0_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_7_0_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_7_0_patch2">CMSSW_3_7_0_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_7_0_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_7_0_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_7_0_patch1">CMSSW_3_7_0_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_7_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_7_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_7_0">CMSSW_3_7_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_6_3_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_6_3_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_6_3_patch2">CMSSW_3_6_3_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_6_3_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_6_3_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_6_3_patch1">CMSSW_3_6_3_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_6_3_hltpatch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_6_3_hltpatch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_6_3_hltpatch4">CMSSW_3_6_3_hltpatch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_6_3_SLHC1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_6_3_SLHC1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_6_3_SLHC1">CMSSW_3_6_3_SLHC1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_6_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_6_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_6_3">CMSSW_3_6_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_6_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_6_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_6_2">CMSSW_3_6_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_6_1_patch7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_6_1_patch7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_6_1_patch7">CMSSW_3_6_1_patch7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_6_1_patch6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_6_1_patch6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_6_1_patch6">CMSSW_3_6_1_patch6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_6_1_patch5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_6_1_patch5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_6_1_patch5">CMSSW_3_6_1_patch5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_6_1_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_6_1_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_6_1_patch4">CMSSW_3_6_1_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_6_1_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_6_1_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_6_1_patch3">CMSSW_3_6_1_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_6_1_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_6_1_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_6_1_patch1">CMSSW_3_6_1_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_6_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_6_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_6_1">CMSSW_3_6_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_6_0_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_6_0_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_6_0_patch2">CMSSW_3_6_0_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_6_0_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_6_0_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_6_0_patch1">CMSSW_3_6_0_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_6_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_6_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_6_0">CMSSW_3_6_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_8_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_8_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_8_patch4">CMSSW_3_5_8_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_8_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_8_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_8_patch3">CMSSW_3_5_8_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_8_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_8_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_8_patch2">CMSSW_3_5_8_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_8_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_8_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_8_patch1">CMSSW_3_5_8_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_8/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_8">CMSSW_3_5_8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_7_hltpatch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_7_hltpatch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_7_hltpatch4">CMSSW_3_5_7_hltpatch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_7">CMSSW_3_5_7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_6_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_6_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_6_patch1">CMSSW_3_5_6_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_6">CMSSW_3_5_6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_5">CMSSW_3_5_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_4_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_4_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_4_patch2">CMSSW_3_5_4_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_4_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_4_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_4_patch1">CMSSW_3_5_4_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_4">CMSSW_3_5_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_3">CMSSW_3_5_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_2_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_2_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_2_patch2">CMSSW_3_5_2_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_2_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_2_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_2_patch1">CMSSW_3_5_2_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_2">CMSSW_3_5_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_1_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_1_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_1_patch1">CMSSW_3_5_1_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_1">CMSSW_3_5_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_0_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_0_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_0_patch1">CMSSW_3_5_0_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_5_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_5_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_5_0">CMSSW_3_5_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_4_2_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_4_2_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_4_2_patch1">CMSSW_3_4_2_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_4_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_4_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_4_2">CMSSW_3_4_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_4_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_4_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_4_1">CMSSW_3_4_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_4_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_4_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_4_0">CMSSW_3_4_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_3_6_patch6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_3_6_patch6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_3_6_patch6">CMSSW_3_3_6_patch6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_3_6_patch5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_3_6_patch5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_3_6_patch5">CMSSW_3_3_6_patch5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_3_6_patch4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_3_6_patch4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_3_6_patch4">CMSSW_3_3_6_patch4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_3_6_patch3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_3_6_patch3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_3_6_patch3">CMSSW_3_3_6_patch3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_3_6_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_3_6_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_3_6_patch2">CMSSW_3_3_6_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_3_6_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_3_6_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_3_6_patch1">CMSSW_3_3_6_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_3_6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_3_6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_3_6">CMSSW_3_3_6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_3_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_3_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_3_5">CMSSW_3_3_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_3_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_3_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_3_4">CMSSW_3_3_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_3_3_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_3_3_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_3_3_patch1">CMSSW_3_3_3_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_3_3_TSG/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_3_3_TSG"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_3_3_TSG">CMSSW_3_3_3_TSG</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_3_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_3_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_3_3">CMSSW_3_3_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_3_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_3_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_3_2">CMSSW_3_3_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_3_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_3_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_3_1">CMSSW_3_3_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_3_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_3_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_3_0">CMSSW_3_3_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_2_8/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_2_8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_2_8">CMSSW_3_2_8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_2_7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_2_7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_2_7">CMSSW_3_2_7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_2_6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_2_6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_2_6">CMSSW_3_2_6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_2_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_2_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_2_5">CMSSW_3_2_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_2_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_2_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_2_4">CMSSW_3_2_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_2_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_2_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_2_3">CMSSW_3_2_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_2_2_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_2_2_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_2_2_patch2">CMSSW_3_2_2_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_2_2_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_2_2_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_2_2_patch1">CMSSW_3_2_2_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_2_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_2_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_2_2">CMSSW_3_2_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_2_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_2_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_2_1">CMSSW_3_2_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_2_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_2_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_2_0">CMSSW_3_2_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_1_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_1_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_1_4">CMSSW_3_1_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_1_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_1_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_1_3">CMSSW_3_1_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_1_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_1_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_1_2">CMSSW_3_1_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_1_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_1_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_1_1">CMSSW_3_1_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_1_0_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_1_0_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_1_0_patch1">CMSSW_3_1_0_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_3_1_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_3_1_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_3_1_0">CMSSW_3_1_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_13_offpatch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_13_offpatch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_13_offpatch1">CMSSW_2_2_13_offpatch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_13_HLT/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_13_HLT"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_13_HLT">CMSSW_2_2_13_HLT</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_13/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_13"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_13">CMSSW_2_2_13</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_12_HLT/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_12_HLT"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_12_HLT">CMSSW_2_2_12_HLT</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_12/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_12"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_12">CMSSW_2_2_12</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_11_offpatch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_11_offpatch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_11_offpatch1">CMSSW_2_2_11_offpatch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_11_HLT/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_11_HLT"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_11_HLT">CMSSW_2_2_11_HLT</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_11/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_11"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_11">CMSSW_2_2_11</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_10_HLT/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_10_HLT"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_10_HLT">CMSSW_2_2_10_HLT</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_10/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_10">CMSSW_2_2_10</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_9/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_9">CMSSW_2_2_9</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_8/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_8">CMSSW_2_2_8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_7">CMSSW_2_2_7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_6_HLT/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_6_HLT"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_6_HLT">CMSSW_2_2_6_HLT</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_6">CMSSW_2_2_6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_5">CMSSW_2_2_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_4">CMSSW_2_2_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_3">CMSSW_2_2_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_2">CMSSW_2_2_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_1">CMSSW_2_2_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_2_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_2_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_2_0">CMSSW_2_2_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_1_19/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_1_19"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_1_19">CMSSW_2_1_19</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_1_17/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_1_17"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_1_17">CMSSW_2_1_17</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_1_12/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_1_12"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_1_12">CMSSW_2_1_12</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_1_11/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_1_11"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_1_11">CMSSW_2_1_11</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_1_10_patch2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_1_10_patch2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_1_10_patch2">CMSSW_2_1_10_patch2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_1_10_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_1_10_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_1_10_patch1">CMSSW_2_1_10_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_1_10/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_1_10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_1_10">CMSSW_2_1_10</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_1_9/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_1_9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_1_9">CMSSW_2_1_9</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_1_8/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_1_8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_1_8">CMSSW_2_1_8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_1_7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_1_7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_1_7">CMSSW_2_1_7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_1_6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_1_6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_1_6">CMSSW_2_1_6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_1_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_1_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_1_5">CMSSW_2_1_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_1_4_patch1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_1_4_patch1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_1_4_patch1">CMSSW_2_1_4_patch1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_1_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_1_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_1_3">CMSSW_2_1_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_1_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_1_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_1_2">CMSSW_2_1_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_1_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_1_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_1_1">CMSSW_2_1_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_1_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_1_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_1_0">CMSSW_2_1_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_0_12/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_0_12"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_0_12">CMSSW_2_0_12</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_0_11/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_0_11"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_0_11">CMSSW_2_0_11</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_0_10/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_0_10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_0_10">CMSSW_2_0_10</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_0_9/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_0_9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_0_9">CMSSW_2_0_9</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_0_8/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_0_8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_0_8">CMSSW_2_0_8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_0_7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_0_7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_0_7">CMSSW_2_0_7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_0_6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_0_6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_0_6">CMSSW_2_0_6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_0_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_0_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_0_5">CMSSW_2_0_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_0_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_0_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_0_4">CMSSW_2_0_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_0_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_0_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_0_3">CMSSW_2_0_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_0_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_0_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_0_2">CMSSW_2_0_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_0_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_0_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_0_1">CMSSW_2_0_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_2_0_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_2_0_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_2_0_0">CMSSW_2_0_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_8_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_8_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_8_4">CMSSW_1_8_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_8_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_8_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_8_3">CMSSW_1_8_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_8_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_8_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_8_2">CMSSW_1_8_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_8_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_8_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_8_1">CMSSW_1_8_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_8_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_8_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_8_0">CMSSW_1_8_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_7_7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_7_7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_7_7">CMSSW_1_7_7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_7_6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_7_6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_7_6">CMSSW_1_7_6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_7_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_7_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_7_5">CMSSW_1_7_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_7_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_7_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_7_4">CMSSW_1_7_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_7_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_7_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_7_3">CMSSW_1_7_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_7_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_7_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_7_2">CMSSW_1_7_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_7_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_7_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_7_1">CMSSW_1_7_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_7_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_7_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_7_0">CMSSW_1_7_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_6_12/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_6_12"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_6_12">CMSSW_1_6_12</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_6_11/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_6_11"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_6_11">CMSSW_1_6_11</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_6_10/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_6_10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_6_10">CMSSW_1_6_10</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_6_9/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_6_9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_6_9">CMSSW_1_6_9</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_6_8/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_6_8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_6_8">CMSSW_1_6_8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_6_7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_6_7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_6_7">CMSSW_1_6_7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_6_6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_6_6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_6_6">CMSSW_1_6_6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_6_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_6_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_6_5">CMSSW_1_6_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_6_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_6_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_6_4">CMSSW_1_6_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_6_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_6_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_6_3">CMSSW_1_6_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_6_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_6_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_6_1">CMSSW_1_6_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_6_0_DAQ3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_6_0_DAQ3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_6_0_DAQ3">CMSSW_1_6_0_DAQ3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_6_0_DAQ1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_6_0_DAQ1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_6_0_DAQ1">CMSSW_1_6_0_DAQ1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_5_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_5_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_5_4">CMSSW_1_5_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_5_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_5_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_5_3">CMSSW_1_5_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_5_2_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_5_2_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_5_2_1">CMSSW_1_5_2_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_5_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_5_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_5_2">CMSSW_1_5_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_5_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_5_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_5_1">CMSSW_1_5_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_5_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_5_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_5_0">CMSSW_1_5_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_4_10/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_4_10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_4_10">CMSSW_1_4_10</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_4_9/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_4_9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_4_9">CMSSW_1_4_9</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_4_8/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_4_8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_4_8">CMSSW_1_4_8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_4_7/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_4_7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_4_7">CMSSW_1_4_7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_4_6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_4_6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_4_6">CMSSW_1_4_6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_4_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_4_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_4_5">CMSSW_1_4_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_4_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_4_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_4_4">CMSSW_1_4_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_4_3g483/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_4_3g483"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_4_3g483">CMSSW_1_4_3g483</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_4_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_4_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_4_3">CMSSW_1_4_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_4_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_4_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_4_2">CMSSW_1_4_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_4_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_4_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_4_1">CMSSW_1_4_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_4_0_DAQ1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_4_0_DAQ1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_4_0_DAQ1">CMSSW_1_4_0_DAQ1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_4_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_4_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_4_0">CMSSW_1_4_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_3_6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_3_6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_3_6">CMSSW_1_3_6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_3_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_3_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_3_5">CMSSW_1_3_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_3_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_3_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_3_4">CMSSW_1_3_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_3_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_3_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_3_3">CMSSW_1_3_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_3_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_3_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_3_2">CMSSW_1_3_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_3_1_HLT6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_3_1_HLT6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_3_1_HLT6">CMSSW_1_3_1_HLT6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_3_1_HLT5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_3_1_HLT5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_3_1_HLT5">CMSSW_1_3_1_HLT5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_3_1_HLT4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_3_1_HLT4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_3_1_HLT4">CMSSW_1_3_1_HLT4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_3_1_HLT3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_3_1_HLT3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_3_1_HLT3">CMSSW_1_3_1_HLT3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_3_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_3_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_3_1">CMSSW_1_3_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_3_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_3_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_3_0">CMSSW_1_3_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_2_6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_2_6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_2_6">CMSSW_1_2_6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_2_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_2_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_2_5">CMSSW_1_2_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_2_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_2_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_2_4">CMSSW_1_2_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_2_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_2_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_2_3">CMSSW_1_2_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_2_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_2_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_2_2">CMSSW_1_2_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_2_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_2_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_2_1">CMSSW_1_2_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_2_0_g4_82p01/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_2_0_g4_82p01"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_2_0_g4_82p01">CMSSW_1_2_0_g4_82p01</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_2_0_g4_82/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_2_0_g4_82"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_2_0_g4_82">CMSSW_1_2_0_g4_82</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_2_0_g4_81/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_2_0_g4_81"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_2_0_g4_81">CMSSW_1_2_0_g4_81</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_2_0_SL4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_2_0_SL4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_2_0_SL4">CMSSW_1_2_0_SL4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_2_0_4821/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_2_0_4821"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_2_0_4821">CMSSW_1_2_0_4821</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_1_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_1_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_1_2">CMSSW_1_1_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_1_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_1_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_1_1">CMSSW_1_1_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_1_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_1_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_1_0">CMSSW_1_1_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_0_6/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_0_6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_0_6">CMSSW_1_0_6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_0_5/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_0_5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_0_5">CMSSW_1_0_5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_0_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_0_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_0_4">CMSSW_1_0_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_0_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_0_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_0_3">CMSSW_1_0_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_0_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_0_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_0_2">CMSSW_1_0_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_0_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_0_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_0_1">CMSSW_1_0_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_0_0_g4_81/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_0_0_g4_81"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_0_0_g4_81">CMSSW_1_0_0_g4_81</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_1_0_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_1_0_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_1_0_0">CMSSW_1_0_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_9_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_9_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_9_2">CMSSW_0_9_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_9_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_9_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_9_1">CMSSW_0_9_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_9_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_9_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_9_0">CMSSW_0_9_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_8_4/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_8_4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_8_4">CMSSW_0_8_4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_8_3/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_8_3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_8_3">CMSSW_0_8_3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_8_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_8_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_8_2">CMSSW_0_8_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_8_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_8_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_8_1">CMSSW_0_8_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_8_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_8_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_8_0">CMSSW_0_8_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_7_2/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_7_2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_7_2">CMSSW_0_7_2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_7_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_7_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_7_1">CMSSW_0_7_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_7_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_7_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_7_0">CMSSW_0_7_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_6_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_6_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_6_1">CMSSW_0_6_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_6_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_6_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_6_0">CMSSW_0_6_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_5_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_5_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_5_1">CMSSW_0_5_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_4_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_4_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_4_1">CMSSW_0_4_1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_4_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_4_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_4_0">CMSSW_0_4_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_3_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_3_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_3_0">CMSSW_0_3_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_2_fake/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_2_fake"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_2_fake">CMSSW_0_2_fake</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_2_0_condtest/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_2_0_condtest"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_2_0_condtest">CMSSW_0_2_0_condtest</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_2_0/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_2_0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_2_0">CMSSW_0_2_0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/oiorio/cmssw/tree/CMSSW_0_0_1/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                 data-name="CMSSW_0_0_1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="CMSSW_0_0_1">CMSSW_0_0_1</a>
            </div> <!-- /.select-menu-item -->
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/oiorio/cmssw/tree/CMSSW_5_3_X" data-branch="CMSSW_5_3_X" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">cmssw</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/oiorio/cmssw/tree/CMSSW_5_3_X/TopQuarkAnalysis" data-branch="CMSSW_5_3_X" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">TopQuarkAnalysis</span></a></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/oiorio/cmssw/tree/CMSSW_5_3_X/TopQuarkAnalysis/SingleTop" data-branch="CMSSW_5_3_X" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">SingleTop</span></a></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/oiorio/cmssw/tree/CMSSW_5_3_X/TopQuarkAnalysis/SingleTop/test" data-branch="CMSSW_5_3_X" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">test</span></a></span><span class="separator"> / </span><strong class="final-path">SingleTopSkim_TChannel_cfg.py</strong> <span class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>



  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://0.gravatar.com/avatar/2bf345cf93ede198cad8e7b692c8a029?d=https%3A%2F%2Fidenticons.github.com%2Fa58d9383c89da628d9f511365958978d.png&amp;r=x&amp;s=140" width="24" />
    <span class="author"><a href="/oiorio" rel="author">oiorio</a></span>
    <time class="js-relative-date" datetime="2014-01-02T11:22:45-08:00" title="2014-01-02 11:22:45">January 02, 2014</time>
    <div class="commit-title">
        <a href="/oiorio/cmssw/commit/57ab374c1d3a6ed75e02fb29a13c57ccc78347d2" class="message" data-pjax="true" title="added single top packages">added single top packages</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong> contributor</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img height="24" src="https://0.gravatar.com/avatar/2bf345cf93ede198cad8e7b692c8a029?d=https%3A%2F%2Fidenticons.github.com%2Fa58d9383c89da628d9f511365958978d.png&amp;r=x&amp;s=140" width="24" />
            <a href="/oiorio">oiorio</a>
          </li>
      </ul>
    </div>
  </div>

<div id="files" class="bubble">
  <div class="file">
    <div class="meta">
      <div class="info">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
          <span>625 lines (507 sloc)</span>
        <span>24.065 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
                <a class="minibutton"
                   href="/oiorio/cmssw/edit/CMSSW_5_3_X/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
                   data-method="post" rel="nofollow" data-hotkey="e">Edit</a>
          <a href="/oiorio/cmssw/raw/CMSSW_5_3_X/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/oiorio/cmssw/blame/CMSSW_5_3_X/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py" class="button minibutton ">Blame</a>
          <a href="/oiorio/cmssw/commits/CMSSW_5_3_X/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
          <a class="minibutton danger empty-icon tooltipped downwards"
             href="/oiorio/cmssw/delete/CMSSW_5_3_X/TopQuarkAnalysis/SingleTop/test/SingleTopSkim_TChannel_cfg.py"
             title=""
             data-method="post" data-test-id="delete-blob-file" rel="nofollow">
          Delete
        </a>
      </div><!-- /.actions -->

    </div>
        <div class="blob-wrapper data type-python js-blob-data">
        <table class="file-code file-diff">
          <tr class="file-code-line">
            <td class="blob-line-nums">
              <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
<span id="L371" rel="#L371">371</span>
<span id="L372" rel="#L372">372</span>
<span id="L373" rel="#L373">373</span>
<span id="L374" rel="#L374">374</span>
<span id="L375" rel="#L375">375</span>
<span id="L376" rel="#L376">376</span>
<span id="L377" rel="#L377">377</span>
<span id="L378" rel="#L378">378</span>
<span id="L379" rel="#L379">379</span>
<span id="L380" rel="#L380">380</span>
<span id="L381" rel="#L381">381</span>
<span id="L382" rel="#L382">382</span>
<span id="L383" rel="#L383">383</span>
<span id="L384" rel="#L384">384</span>
<span id="L385" rel="#L385">385</span>
<span id="L386" rel="#L386">386</span>
<span id="L387" rel="#L387">387</span>
<span id="L388" rel="#L388">388</span>
<span id="L389" rel="#L389">389</span>
<span id="L390" rel="#L390">390</span>
<span id="L391" rel="#L391">391</span>
<span id="L392" rel="#L392">392</span>
<span id="L393" rel="#L393">393</span>
<span id="L394" rel="#L394">394</span>
<span id="L395" rel="#L395">395</span>
<span id="L396" rel="#L396">396</span>
<span id="L397" rel="#L397">397</span>
<span id="L398" rel="#L398">398</span>
<span id="L399" rel="#L399">399</span>
<span id="L400" rel="#L400">400</span>
<span id="L401" rel="#L401">401</span>
<span id="L402" rel="#L402">402</span>
<span id="L403" rel="#L403">403</span>
<span id="L404" rel="#L404">404</span>
<span id="L405" rel="#L405">405</span>
<span id="L406" rel="#L406">406</span>
<span id="L407" rel="#L407">407</span>
<span id="L408" rel="#L408">408</span>
<span id="L409" rel="#L409">409</span>
<span id="L410" rel="#L410">410</span>
<span id="L411" rel="#L411">411</span>
<span id="L412" rel="#L412">412</span>
<span id="L413" rel="#L413">413</span>
<span id="L414" rel="#L414">414</span>
<span id="L415" rel="#L415">415</span>
<span id="L416" rel="#L416">416</span>
<span id="L417" rel="#L417">417</span>
<span id="L418" rel="#L418">418</span>
<span id="L419" rel="#L419">419</span>
<span id="L420" rel="#L420">420</span>
<span id="L421" rel="#L421">421</span>
<span id="L422" rel="#L422">422</span>
<span id="L423" rel="#L423">423</span>
<span id="L424" rel="#L424">424</span>
<span id="L425" rel="#L425">425</span>
<span id="L426" rel="#L426">426</span>
<span id="L427" rel="#L427">427</span>
<span id="L428" rel="#L428">428</span>
<span id="L429" rel="#L429">429</span>
<span id="L430" rel="#L430">430</span>
<span id="L431" rel="#L431">431</span>
<span id="L432" rel="#L432">432</span>
<span id="L433" rel="#L433">433</span>
<span id="L434" rel="#L434">434</span>
<span id="L435" rel="#L435">435</span>
<span id="L436" rel="#L436">436</span>
<span id="L437" rel="#L437">437</span>
<span id="L438" rel="#L438">438</span>
<span id="L439" rel="#L439">439</span>
<span id="L440" rel="#L440">440</span>
<span id="L441" rel="#L441">441</span>
<span id="L442" rel="#L442">442</span>
<span id="L443" rel="#L443">443</span>
<span id="L444" rel="#L444">444</span>
<span id="L445" rel="#L445">445</span>
<span id="L446" rel="#L446">446</span>
<span id="L447" rel="#L447">447</span>
<span id="L448" rel="#L448">448</span>
<span id="L449" rel="#L449">449</span>
<span id="L450" rel="#L450">450</span>
<span id="L451" rel="#L451">451</span>
<span id="L452" rel="#L452">452</span>
<span id="L453" rel="#L453">453</span>
<span id="L454" rel="#L454">454</span>
<span id="L455" rel="#L455">455</span>
<span id="L456" rel="#L456">456</span>
<span id="L457" rel="#L457">457</span>
<span id="L458" rel="#L458">458</span>
<span id="L459" rel="#L459">459</span>
<span id="L460" rel="#L460">460</span>
<span id="L461" rel="#L461">461</span>
<span id="L462" rel="#L462">462</span>
<span id="L463" rel="#L463">463</span>
<span id="L464" rel="#L464">464</span>
<span id="L465" rel="#L465">465</span>
<span id="L466" rel="#L466">466</span>
<span id="L467" rel="#L467">467</span>
<span id="L468" rel="#L468">468</span>
<span id="L469" rel="#L469">469</span>
<span id="L470" rel="#L470">470</span>
<span id="L471" rel="#L471">471</span>
<span id="L472" rel="#L472">472</span>
<span id="L473" rel="#L473">473</span>
<span id="L474" rel="#L474">474</span>
<span id="L475" rel="#L475">475</span>
<span id="L476" rel="#L476">476</span>
<span id="L477" rel="#L477">477</span>
<span id="L478" rel="#L478">478</span>
<span id="L479" rel="#L479">479</span>
<span id="L480" rel="#L480">480</span>
<span id="L481" rel="#L481">481</span>
<span id="L482" rel="#L482">482</span>
<span id="L483" rel="#L483">483</span>
<span id="L484" rel="#L484">484</span>
<span id="L485" rel="#L485">485</span>
<span id="L486" rel="#L486">486</span>
<span id="L487" rel="#L487">487</span>
<span id="L488" rel="#L488">488</span>
<span id="L489" rel="#L489">489</span>
<span id="L490" rel="#L490">490</span>
<span id="L491" rel="#L491">491</span>
<span id="L492" rel="#L492">492</span>
<span id="L493" rel="#L493">493</span>
<span id="L494" rel="#L494">494</span>
<span id="L495" rel="#L495">495</span>
<span id="L496" rel="#L496">496</span>
<span id="L497" rel="#L497">497</span>
<span id="L498" rel="#L498">498</span>
<span id="L499" rel="#L499">499</span>
<span id="L500" rel="#L500">500</span>
<span id="L501" rel="#L501">501</span>
<span id="L502" rel="#L502">502</span>
<span id="L503" rel="#L503">503</span>
<span id="L504" rel="#L504">504</span>
<span id="L505" rel="#L505">505</span>
<span id="L506" rel="#L506">506</span>
<span id="L507" rel="#L507">507</span>
<span id="L508" rel="#L508">508</span>
<span id="L509" rel="#L509">509</span>
<span id="L510" rel="#L510">510</span>
<span id="L511" rel="#L511">511</span>
<span id="L512" rel="#L512">512</span>
<span id="L513" rel="#L513">513</span>
<span id="L514" rel="#L514">514</span>
<span id="L515" rel="#L515">515</span>
<span id="L516" rel="#L516">516</span>
<span id="L517" rel="#L517">517</span>
<span id="L518" rel="#L518">518</span>
<span id="L519" rel="#L519">519</span>
<span id="L520" rel="#L520">520</span>
<span id="L521" rel="#L521">521</span>
<span id="L522" rel="#L522">522</span>
<span id="L523" rel="#L523">523</span>
<span id="L524" rel="#L524">524</span>
<span id="L525" rel="#L525">525</span>
<span id="L526" rel="#L526">526</span>
<span id="L527" rel="#L527">527</span>
<span id="L528" rel="#L528">528</span>
<span id="L529" rel="#L529">529</span>
<span id="L530" rel="#L530">530</span>
<span id="L531" rel="#L531">531</span>
<span id="L532" rel="#L532">532</span>
<span id="L533" rel="#L533">533</span>
<span id="L534" rel="#L534">534</span>
<span id="L535" rel="#L535">535</span>
<span id="L536" rel="#L536">536</span>
<span id="L537" rel="#L537">537</span>
<span id="L538" rel="#L538">538</span>
<span id="L539" rel="#L539">539</span>
<span id="L540" rel="#L540">540</span>
<span id="L541" rel="#L541">541</span>
<span id="L542" rel="#L542">542</span>
<span id="L543" rel="#L543">543</span>
<span id="L544" rel="#L544">544</span>
<span id="L545" rel="#L545">545</span>
<span id="L546" rel="#L546">546</span>
<span id="L547" rel="#L547">547</span>
<span id="L548" rel="#L548">548</span>
<span id="L549" rel="#L549">549</span>
<span id="L550" rel="#L550">550</span>
<span id="L551" rel="#L551">551</span>
<span id="L552" rel="#L552">552</span>
<span id="L553" rel="#L553">553</span>
<span id="L554" rel="#L554">554</span>
<span id="L555" rel="#L555">555</span>
<span id="L556" rel="#L556">556</span>
<span id="L557" rel="#L557">557</span>
<span id="L558" rel="#L558">558</span>
<span id="L559" rel="#L559">559</span>
<span id="L560" rel="#L560">560</span>
<span id="L561" rel="#L561">561</span>
<span id="L562" rel="#L562">562</span>
<span id="L563" rel="#L563">563</span>
<span id="L564" rel="#L564">564</span>
<span id="L565" rel="#L565">565</span>
<span id="L566" rel="#L566">566</span>
<span id="L567" rel="#L567">567</span>
<span id="L568" rel="#L568">568</span>
<span id="L569" rel="#L569">569</span>
<span id="L570" rel="#L570">570</span>
<span id="L571" rel="#L571">571</span>
<span id="L572" rel="#L572">572</span>
<span id="L573" rel="#L573">573</span>
<span id="L574" rel="#L574">574</span>
<span id="L575" rel="#L575">575</span>
<span id="L576" rel="#L576">576</span>
<span id="L577" rel="#L577">577</span>
<span id="L578" rel="#L578">578</span>
<span id="L579" rel="#L579">579</span>
<span id="L580" rel="#L580">580</span>
<span id="L581" rel="#L581">581</span>
<span id="L582" rel="#L582">582</span>
<span id="L583" rel="#L583">583</span>
<span id="L584" rel="#L584">584</span>
<span id="L585" rel="#L585">585</span>
<span id="L586" rel="#L586">586</span>
<span id="L587" rel="#L587">587</span>
<span id="L588" rel="#L588">588</span>
<span id="L589" rel="#L589">589</span>
<span id="L590" rel="#L590">590</span>
<span id="L591" rel="#L591">591</span>
<span id="L592" rel="#L592">592</span>
<span id="L593" rel="#L593">593</span>
<span id="L594" rel="#L594">594</span>
<span id="L595" rel="#L595">595</span>
<span id="L596" rel="#L596">596</span>
<span id="L597" rel="#L597">597</span>
<span id="L598" rel="#L598">598</span>
<span id="L599" rel="#L599">599</span>
<span id="L600" rel="#L600">600</span>
<span id="L601" rel="#L601">601</span>
<span id="L602" rel="#L602">602</span>
<span id="L603" rel="#L603">603</span>
<span id="L604" rel="#L604">604</span>
<span id="L605" rel="#L605">605</span>
<span id="L606" rel="#L606">606</span>
<span id="L607" rel="#L607">607</span>
<span id="L608" rel="#L608">608</span>
<span id="L609" rel="#L609">609</span>
<span id="L610" rel="#L610">610</span>
<span id="L611" rel="#L611">611</span>
<span id="L612" rel="#L612">612</span>
<span id="L613" rel="#L613">613</span>
<span id="L614" rel="#L614">614</span>
<span id="L615" rel="#L615">615</span>
<span id="L616" rel="#L616">616</span>
<span id="L617" rel="#L617">617</span>
<span id="L618" rel="#L618">618</span>
<span id="L619" rel="#L619">619</span>
<span id="L620" rel="#L620">620</span>
<span id="L621" rel="#L621">621</span>
<span id="L622" rel="#L622">622</span>
<span id="L623" rel="#L623">623</span>
<span id="L624" rel="#L624">624</span>

            </td>
            <td class="blob-line-code">
                    <div class="code-body highlight"><pre><div class='line' id='LC1'><span class="kn">import</span> <span class="nn">FWCore.ParameterSet.Config</span> <span class="kn">as</span> <span class="nn">cms</span></div><div class='line' id='LC2'><br/></div><div class='line' id='LC3'><span class="c">#Process name:</span></div><div class='line' id='LC4'><span class="n">process</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">Process</span><span class="p">(</span><span class="s">&quot;SingleTop&quot;</span><span class="p">)</span></div><div class='line' id='LC5'><br/></div><div class='line' id='LC6'><span class="c">#MessageLogger options:</span></div><div class='line' id='LC7'><span class="n">process</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s">&quot;FWCore.MessageLogger.MessageLogger_cfi&quot;</span><span class="p">)</span></div><div class='line' id='LC8'><br/></div><div class='line' id='LC9'><span class="n">process</span><span class="o">.</span><span class="n">options</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">untracked</span><span class="o">.</span><span class="n">PSet</span><span class="p">(</span></div><div class='line' id='LC10'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">wantSummary</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">untracked</span><span class="o">.</span><span class="n">bool</span><span class="p">(</span><span class="bp">True</span><span class="p">),</span></div><div class='line' id='LC11'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">FailPath</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">untracked</span><span class="o">.</span><span class="n">vstring</span><span class="p">(</span><span class="s">&#39;ProductNotFound&#39;</span><span class="p">,</span><span class="s">&#39;Type Mismatch&#39;</span><span class="p">)</span></div><div class='line' id='LC12'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC13'><br/></div><div class='line' id='LC14'><span class="c">#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(20) )</span></div><div class='line' id='LC15'><span class="n">process</span><span class="o">.</span><span class="n">maxEvents</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">untracked</span><span class="o">.</span><span class="n">PSet</span><span class="p">(</span> <span class="nb">input</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">untracked</span><span class="o">.</span><span class="n">int32</span><span class="p">(</span><span class="mi">2000</span><span class="p">)</span> <span class="p">)</span></div><div class='line' id='LC16'><span class="c">#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )</span></div><div class='line' id='LC17'><br/></div><div class='line' id='LC18'><span class="n">ChannelName</span> <span class="o">=</span> <span class="s">&quot;TChannel&quot;</span></div><div class='line' id='LC19'><br/></div><div class='line' id='LC20'><span class="c">#Data or MC:</span></div><div class='line' id='LC21'><span class="n">isData</span><span class="o">=</span><span class="bp">False</span></div><div class='line' id='LC22'><br/></div><div class='line' id='LC23'><span class="c">#Input file:</span></div><div class='line' id='LC24'><span class="n">process</span><span class="o">.</span><span class="n">source</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">Source</span> <span class="p">(</span></div><div class='line' id='LC25'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;PoolSource&quot;</span><span class="p">,</span></div><div class='line' id='LC26'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fileNames</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">untracked</span><span class="o">.</span><span class="n">vstring</span> <span class="p">(</span></div><div class='line' id='LC27'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;file:/afs/cern.ch/work/o/oiorio/public/xFrancescoFab/T_t-channel_Synch.root&quot;</span></div><div class='line' id='LC28'><span class="c">#      &quot;file:/afs/cern.ch/work/o/oiorio/public/xFrancescoFab/DataReRecoA.root&quot;</span></div><div class='line' id='LC29'><span class="c">#      &quot;file:8425E88A-AED7-E211-8067-002481E14F5C.root&quot;</span></div><div class='line' id='LC30'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">),</span></div><div class='line' id='LC31'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">duplicateCheckMode</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">untracked</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&#39;noDuplicateCheck&#39;</span><span class="p">)</span></div><div class='line' id='LC32'><span class="p">)</span></div><div class='line' id='LC33'><br/></div><div class='line' id='LC34'><span class="k">if</span> <span class="n">isData</span><span class="p">:</span> <span class="n">process</span><span class="o">.</span><span class="n">source</span><span class="o">.</span><span class="n">fileNames</span><span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">untracked</span><span class="o">.</span><span class="n">vstring</span> <span class="p">(</span> <span class="s">&quot;file:/afs/cern.ch/work/o/oiorio/public/xFrancescoFab/DataReRecoA.root&quot;</span> <span class="p">)</span></div><div class='line' id='LC35'><br/></div><div class='line' id='LC36'><span class="c">#process.MessageLogger.cerr.FwkReport.reportEvery = 100</span></div><div class='line' id='LC37'><br/></div><div class='line' id='LC38'><span class="c">#Include the hermetic top projection: </span></div><div class='line' id='LC39'><span class="n">hermeticTopProjection</span><span class="o">=</span><span class="bp">True</span></div><div class='line' id='LC40'><br/></div><div class='line' id='LC41'><span class="c">#Gsf electron or PF electron: </span></div><div class='line' id='LC42'><span class="n">doGsfElectrons</span><span class="o">=</span><span class="bp">False</span></div><div class='line' id='LC43'><br/></div><div class='line' id='LC44'><span class="c">#Add nJ &gt;= 2 cut: </span></div><div class='line' id='LC45'><span class="n">addJetsCut</span><span class="o">=</span><span class="bp">True</span> </div><div class='line' id='LC46'><br/></div><div class='line' id='LC47'><span class="c">#Run JetMET uncertainties from JME tool</span></div><div class='line' id='LC48'><span class="n">doRunMETUncertainties</span><span class="o">=</span><span class="bp">True</span></div><div class='line' id='LC49'><br/></div><div class='line' id='LC50'><span class="c">#Enable PF taus (true = default: adds the PF tau objects;false = embed them in jets)</span></div><div class='line' id='LC51'><span class="n">EnablePFTaus</span><span class="o">=</span><span class="bp">False</span></div><div class='line' id='LC52'><br/></div><div class='line' id='LC53'><span class="c">#Geometry:</span></div><div class='line' id='LC54'><span class="n">process</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s">&quot;Configuration.Geometry.GeometryIdeal_cff&quot;</span><span class="p">)</span></div><div class='line' id='LC55'><span class="n">process</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s">&quot;Configuration.StandardSequences.FrontierConditions_GlobalTag_cff&quot;</span><span class="p">)</span></div><div class='line' id='LC56'><span class="n">process</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s">&quot;Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff&quot;</span><span class="p">)</span> <span class="c">### real data</span></div><div class='line' id='LC57'><br/></div><div class='line' id='LC58'><span class="c">#Tag:</span></div><div class='line' id='LC59'><span class="c">### new GT - 10Sept2013</span></div><div class='line' id='LC60'><span class="k">if</span> <span class="n">isData</span><span class="p">:</span>  <span class="n">process</span><span class="o">.</span><span class="n">GlobalTag</span><span class="o">.</span><span class="n">globaltag</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&#39;FT53_V21A_AN6::All&#39;</span><span class="p">)</span></div><div class='line' id='LC61'><span class="k">else</span><span class="p">:</span> <span class="n">process</span><span class="o">.</span><span class="n">GlobalTag</span><span class="o">.</span><span class="n">globaltag</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&#39;START53_V27::All&#39;</span><span class="p">)</span></div><div class='line' id='LC62'><span class="c">#process.GlobalTag.globaltag = cms.string(&#39;FT_53_V6C_AN3::All&#39;)</span></div><div class='line' id='LC63'><br/></div><div class='line' id='LC64'><br/></div><div class='line' id='LC65'><span class="c">###Jet probability calibration used for b-tagging must be rerun in simulation:</span></div><div class='line' id='LC66'><span class="c">### https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagPOG?rev=169#2012_Data_and_MC_EPS13_prescript</span></div><div class='line' id='LC67'><span class="c">###Relevant code snippet is copied from this reference. Note that the calibration in 22Jan2013 rereco of real data is fine.</span></div><div class='line' id='LC68'><br/></div><div class='line' id='LC69'><span class="n">process</span><span class="o">.</span><span class="n">GlobalTag</span><span class="o">.</span><span class="n">toGet</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">VPSet</span><span class="p">(</span></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cms</span><span class="o">.</span><span class="n">PSet</span><span class="p">(</span><span class="n">record</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&quot;BTagTrackProbability2DRcd&quot;</span><span class="p">),</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tag</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&quot;TrackProbabilityCalibration_2D_MC53X_v2&quot;</span><span class="p">),</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">connect</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">untracked</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&quot;frontier://FrontierPrep/CMS_COND_BTAU&quot;</span><span class="p">)),</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cms</span><span class="o">.</span><span class="n">PSet</span><span class="p">(</span><span class="n">record</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&quot;BTagTrackProbability3DRcd&quot;</span><span class="p">),</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tag</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&quot;TrackProbabilityCalibration_3D_MC53X_v2&quot;</span><span class="p">),</span></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">connect</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">untracked</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&quot;frontier://FrontierPrep/CMS_COND_BTAU&quot;</span><span class="p">))</span></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC77'><br/></div><div class='line' id='LC78'><br/></div><div class='line' id='LC79'><br/></div><div class='line' id='LC80'><br/></div><div class='line' id='LC81'><span class="c"># dummy output: needed to avoid crash</span></div><div class='line' id='LC82'><span class="n">process</span><span class="o">.</span><span class="n">out</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">OutputModule</span><span class="p">(</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;PoolOutputModule&quot;</span><span class="p">,</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fileName</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">untracked</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&#39;dummy.root&#39;</span><span class="p">),</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">outputCommands</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">untracked</span><span class="o">.</span><span class="n">vstring</span><span class="p">(</span><span class="s">&quot;&quot;</span><span class="p">),</span></div><div class='line' id='LC86'><span class="p">)</span></div><div class='line' id='LC87'><br/></div><div class='line' id='LC88'><span class="c"># ---&gt; PAT + Single top sequences &lt;---</span></div><div class='line' id='LC89'><span class="n">process</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s">&quot;PhysicsTools.PatAlgos.patSequences_cff&quot;</span><span class="p">)</span> </div><div class='line' id='LC90'><br/></div><div class='line' id='LC91'><span class="c">### Filter on good vertices commented for tH analysis</span></div><div class='line' id='LC92'><span class="n">process</span><span class="o">.</span><span class="n">goodOfflinePrimaryVertices</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">EDFilter</span><span class="p">(</span> <span class="s">&quot;PrimaryVertexObjectFilter&quot;</span> <span class="p">,</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filterParams</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">PSet</span><span class="p">(</span> <span class="n">minNdof</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">double</span><span class="p">(</span> <span class="mf">4.</span> <span class="p">)</span> <span class="p">,</span> <span class="n">maxZ</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">double</span><span class="p">(</span> <span class="mf">24.</span> <span class="p">)</span> <span class="p">,</span> <span class="n">maxRho</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">double</span><span class="p">(</span> <span class="mf">2.</span> <span class="p">)</span> <span class="p">)</span> <span class="p">,</span></div><div class='line' id='LC94'><span class="c">#filter = cms.bool( True) , src = cms.InputTag( &#39;offlinePrimaryVertices&#39; ) )</span></div><div class='line' id='LC95'><span class="nb">filter</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">bool</span><span class="p">(</span> <span class="bp">False</span><span class="p">)</span> <span class="p">,</span> <span class="n">src</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span> <span class="s">&#39;offlinePrimaryVertices&#39;</span> <span class="p">)</span> <span class="p">)</span></div><div class='line' id='LC96'><br/></div><div class='line' id='LC97'><br/></div><div class='line' id='LC98'><br/></div><div class='line' id='LC99'><span class="c"># Configure PAT to use PFBRECO instead of AOD sources</span></div><div class='line' id='LC100'><span class="c"># this function will modify the PAT sequences.</span></div><div class='line' id='LC101'><span class="kn">from</span> <span class="nn">PhysicsTools.PatAlgos.tools.pfTools</span> <span class="kn">import</span> <span class="o">*</span></div><div class='line' id='LC102'><span class="kn">from</span> <span class="nn">PhysicsTools.PatAlgos.tools.trigTools</span> <span class="kn">import</span> <span class="o">*</span></div><div class='line' id='LC103'><span class="kn">from</span> <span class="nn">PhysicsTools.PatUtils.tools.metUncertaintyTools</span> <span class="kn">import</span> <span class="o">*</span></div><div class='line' id='LC104'><br/></div><div class='line' id='LC105'><span class="n">postfix</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></div><div class='line' id='LC106'><span class="n">runOnMC</span> <span class="o">=</span> <span class="ow">not</span><span class="p">(</span><span class="n">isData</span><span class="p">)</span></div><div class='line' id='LC107'><span class="n">jetAlgoName</span> <span class="o">=</span> <span class="s">&quot;AK5&quot;</span></div><div class='line' id='LC108'><br/></div><div class='line' id='LC109'><span class="k">if</span> <span class="n">runOnMC</span><span class="p">:</span><span class="c">#MC</span></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">jetCorrections</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;L1FastJet&#39;</span><span class="p">,</span><span class="s">&#39;L2Relative&#39;</span><span class="p">,</span><span class="s">&#39;L3Absolute&#39;</span><span class="p">]</span></div><div class='line' id='LC111'><span class="k">else</span><span class="p">:</span><span class="c">#Data</span></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">jetCorrections</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;L1FastJet&#39;</span><span class="p">,</span><span class="s">&#39;L2Relative&#39;</span><span class="p">,</span><span class="s">&#39;L3Absolute&#39;</span><span class="p">,</span><span class="s">&#39;L2L3Residual&#39;</span><span class="p">]</span></div><div class='line' id='LC113'><br/></div><div class='line' id='LC114'><span class="c">############ PRINTOUT ###################</span></div><div class='line' id='LC115'><span class="n">sep_line</span> <span class="o">=</span> <span class="s">&quot;-&quot;</span> <span class="o">*</span> <span class="mi">50</span></div><div class='line' id='LC116'><span class="k">print</span> <span class="n">sep_line</span></div><div class='line' id='LC117'><span class="k">print</span> <span class="s">&#39;running the following PFBRECO sequence:&#39;</span></div><div class='line' id='LC118'><span class="k">print</span> <span class="n">jetAlgoName</span></div><div class='line' id='LC119'><span class="k">print</span> <span class="s">&#39;run on MC        : &#39;</span><span class="p">,</span> <span class="n">runOnMC</span></div><div class='line' id='LC120'><span class="k">print</span> <span class="n">sep_line</span></div><div class='line' id='LC121'><span class="k">print</span> <span class="s">&#39;postfix       : &#39;</span><span class="p">,</span> <span class="n">postfix</span></div><div class='line' id='LC122'><span class="k">print</span> <span class="n">sep_line</span></div><div class='line' id='LC123'><span class="k">print</span> <span class="s">&#39;JEC        : &#39;</span><span class="p">,</span> <span class="n">jetCorrections</span></div><div class='line' id='LC124'><span class="k">print</span> <span class="n">sep_line</span></div><div class='line' id='LC125'><span class="c">#########################################</span></div><div class='line' id='LC126'><br/></div><div class='line' id='LC127'><span class="n">usePF2PAT</span><span class="p">(</span><span class="n">process</span><span class="p">,</span> <span class="n">runPF2PAT</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">jetAlgo</span><span class="o">=</span><span class="n">jetAlgoName</span><span class="p">,</span> <span class="n">runOnMC</span><span class="o">=</span><span class="n">runOnMC</span><span class="p">,</span> <span class="n">postfix</span><span class="o">=</span><span class="n">postfix</span><span class="p">,</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">jetCorrections</span><span class="o">=</span><span class="p">(</span><span class="s">&#39;AK5PFchs&#39;</span><span class="p">,</span><span class="n">jetCorrections</span><span class="p">),</span> <span class="n">pvCollection</span><span class="o">=</span><span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&#39;goodOfflinePrimaryVertices&#39;</span><span class="p">),</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># jetCorrections=(&#39;AK5PFchs&#39;,jetCorrections), pvCollection=cms.InputTag(&#39;offlinePrimaryVertices&#39;),</span></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">typeIMetCorrections</span><span class="o">=</span><span class="p">(</span><span class="ow">not</span> <span class="n">doRunMETUncertainties</span><span class="p">))</span></div><div class='line' id='LC131'><br/></div><div class='line' id='LC132'><span class="k">if</span> <span class="n">doRunMETUncertainties</span><span class="p">:</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">PhysicsTools.PatUtils.tools.metUncertaintyTools</span> <span class="kn">import</span> <span class="n">runMEtUncertainties</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">isData</span><span class="p">:</span></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">runMEtUncertainties</span><span class="p">(</span><span class="n">process</span><span class="p">,</span><span class="n">electronCollection</span> <span class="o">=</span> <span class="s">&quot;selectedPatElectrons&quot;</span><span class="p">,</span> <span class="n">doSmearJets</span><span class="o">=</span> <span class="bp">False</span><span class="p">,</span> <span class="n">muonCollection</span> <span class="o">=</span> <span class="s">&quot;selectedPatMuons&quot;</span><span class="p">,</span> <span class="n">tauCollection</span><span class="o">=</span><span class="s">&quot;selectedPatTaus&quot;</span><span class="p">,</span> <span class="n">jetCollection</span> <span class="o">=</span> <span class="s">&quot;selectedPatJets&quot;</span><span class="p">,</span><span class="n">jetCorrLabel</span><span class="o">=</span><span class="s">&quot;L2L3Residual&quot;</span><span class="p">)</span></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patPFMet</span><span class="o">.</span><span class="n">addGenMET</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patPFMetJetEnUp</span><span class="o">.</span><span class="n">addGenMET</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patPFMetJetEnDown</span><span class="o">.</span><span class="n">addGenMET</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patPFMetElectronEnUp</span><span class="o">.</span><span class="n">addGenMET</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patPFMetElectronEnDown</span><span class="o">.</span><span class="n">addGenMET</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patPFMetMuonEnUp</span><span class="o">.</span><span class="n">addGenMET</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patPFMetMuonEnDown</span><span class="o">.</span><span class="n">addGenMET</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patPFMetTauEnUp</span><span class="o">.</span><span class="n">addGenMET</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patPFMetTauEnDown</span><span class="o">.</span><span class="n">addGenMET</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patPFMetTauEnUp</span><span class="o">.</span><span class="n">addGenMET</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patPFMetTauEnDown</span><span class="o">.</span><span class="n">addGenMET</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">runMEtUncertainties</span><span class="p">(</span><span class="n">process</span><span class="p">,</span><span class="n">electronCollection</span> <span class="o">=</span> <span class="s">&quot;selectedPatElectrons&quot;</span><span class="p">,</span> <span class="n">doSmearJets</span><span class="o">=</span> <span class="bp">False</span><span class="p">,</span> <span class="n">muonCollection</span> <span class="o">=</span> <span class="s">&quot;selectedPatMuons&quot;</span><span class="p">,</span> <span class="n">tauCollection</span><span class="o">=</span><span class="s">&quot;selectedPatTaus&quot;</span><span class="p">,</span> <span class="n">jetCollection</span> <span class="o">=</span> <span class="s">&quot;selectedPatJets&quot;</span><span class="p">,)</span></div><div class='line' id='LC149'><br/></div><div class='line' id='LC150'><span class="c"># CONFIGURE LEPTONS for the analysis</span></div><div class='line' id='LC151'><br/></div><div class='line' id='LC152'><br/></div><div class='line' id='LC153'><span class="c"># Use DR = 0.3 for PF electrons:</span></div><div class='line' id='LC154'><span class="n">process</span><span class="o">.</span><span class="n">pfIsolatedElectrons</span><span class="o">.</span><span class="n">isolationValueMapsCharged</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">VInputTag</span><span class="p">(</span><span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;elPFIsoValueCharged03PFId&quot;</span><span class="p">))</span></div><div class='line' id='LC155'><span class="c">#process.pfIsolatedElectrons.deltaBetaIsolationValueMap = cms.InputTag(&quot;elPFIsoValuePU03PFId&quot;)</span></div><div class='line' id='LC156'><span class="n">process</span><span class="o">.</span><span class="n">pfIsolatedElectrons</span><span class="o">.</span><span class="n">isolationValueMapsNeutral</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">VInputTag</span><span class="p">(</span><span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;elPFIsoValueNeutral03PFId&quot;</span><span class="p">),</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;elPFIsoValueGamma03PFId&quot;</span><span class="p">))</span></div><div class='line' id='LC157'><br/></div><div class='line' id='LC158'><br/></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC160'><span class="c"># Switch to GsfElectrons if required</span></div><div class='line' id='LC161'><span class="k">if</span> <span class="n">doGsfElectrons</span><span class="p">:</span></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Gsf Electrons</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Use DR = 0.3:</span></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">useGsfElectrons</span><span class="p">(</span><span class="n">process</span><span class="p">,</span><span class="n">postfix</span><span class="p">,</span><span class="s">&quot;03&quot;</span><span class="p">)</span></div><div class='line' id='LC165'><span class="k">if</span> <span class="ow">not</span><span class="p">(</span><span class="n">doGsfElectrons</span><span class="p">):</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Set Isolation for PAT Electrons</span></div><div class='line' id='LC167'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patElectrons</span><span class="o">.</span><span class="n">isolationValues</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">PSet</span><span class="p">(</span> <span class="n">pfChargedHadrons</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;elPFIsoValueCharged03PFId&quot;</span><span class="p">),</span> <span class="n">pfChargedAll</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;elPFIsoValueChargedAll03PFId&quot;</span><span class="p">),</span> <span class="n">pfPUChargedHadrons</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;elPFIsoValuePU03PFId&quot;</span><span class="p">),</span> <span class="n">pfNeutralHadrons</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;elPFIsoValueNeutral03PFId&quot;</span><span class="p">),</span> <span class="n">pfPhotons</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;elPFIsoValueGamma03PFId&quot;</span><span class="p">)</span> <span class="p">)</span></div><div class='line' id='LC168'><br/></div><div class='line' id='LC169'><span class="c">#Apply PFnoPU:</span></div><div class='line' id='LC170'><span class="n">process</span><span class="o">.</span><span class="n">pfPileUp</span><span class="o">.</span><span class="n">Enable</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC171'><span class="n">process</span><span class="o">.</span><span class="n">pfPileUp</span><span class="o">.</span><span class="n">checkClosestZVertex</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">bool</span><span class="p">(</span><span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC172'><br/></div><div class='line' id='LC173'><span class="c">#Disable top projection for taus</span></div><div class='line' id='LC174'><span class="n">process</span><span class="o">.</span><span class="n">pfNoTau</span><span class="o">.</span><span class="n">enable</span> <span class="o">=</span> <span class="n">EnablePFTaus</span></div><div class='line' id='LC175'><br/></div><div class='line' id='LC176'><span class="c"># Prepare MVA electronId</span></div><div class='line' id='LC177'><span class="n">process</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s">&quot;EgammaAnalysis.ElectronTools.electronIdMVAProducer_cfi&quot;</span><span class="p">)</span></div><div class='line' id='LC178'><span class="n">process</span><span class="o">.</span><span class="n">mvaID</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">Sequence</span><span class="p">(</span>  <span class="n">process</span><span class="o">.</span><span class="n">mvaTrigV0</span> <span class="o">+</span> <span class="n">process</span><span class="o">.</span><span class="n">mvaNonTrigV0</span> <span class="p">)</span></div><div class='line' id='LC179'><span class="n">process</span><span class="o">.</span><span class="n">patElectronIDs</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">Sequence</span><span class="p">(</span> <span class="n">process</span><span class="o">.</span><span class="n">mvaID</span> <span class="p">)</span></div><div class='line' id='LC180'><span class="c"># Add MVA electronId</span></div><div class='line' id='LC181'><span class="n">process</span><span class="o">.</span><span class="n">electronIDSources</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">PSet</span><span class="p">(</span></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">mvaTrigV0</span>    <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;mvaTrigV0&quot;</span><span class="p">),</span></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">mvaNonTrigV0</span>    <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;mvaNonTrigV0&quot;</span><span class="p">)</span></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC185'><br/></div><div class='line' id='LC186'><span class="n">process</span><span class="o">.</span><span class="n">patElectrons</span><span class="o">.</span><span class="n">electronIDSources</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">electronIDSources</span></div><div class='line' id='LC187'><br/></div><div class='line' id='LC188'><span class="c">### Removing request of compatibility with the primary vertex</span></div><div class='line' id='LC189'><span class="c">### Because info on the impact parameter are used in the MVA ID</span></div><div class='line' id='LC190'><span class="c">### https://hypernews.cern.ch/HyperNews/CMS/get/egamma-elecid/72/1.html</span></div><div class='line' id='LC191'><span class="n">process</span><span class="o">.</span><span class="n">pfElectronsFromVertex</span><span class="o">.</span><span class="n">d0Cut</span> <span class="o">=</span> <span class="mf">9999.</span></div><div class='line' id='LC192'><span class="n">process</span><span class="o">.</span><span class="n">pfElectronsFromVertex</span><span class="o">.</span><span class="n">d0SigCut</span> <span class="o">=</span> <span class="mf">9999.</span></div><div class='line' id='LC193'><span class="n">process</span><span class="o">.</span><span class="n">pfElectronsFromVertex</span><span class="o">.</span><span class="n">dzCut</span> <span class="o">=</span> <span class="mf">9999.</span></div><div class='line' id='LC194'><span class="n">process</span><span class="o">.</span><span class="n">pfElectronsFromVertex</span><span class="o">.</span><span class="n">dzSigCut</span> <span class="o">=</span> <span class="mf">9999.</span></div><div class='line' id='LC195'><br/></div><div class='line' id='LC196'><span class="n">process</span><span class="o">.</span><span class="n">pfMuonsFromVertex</span><span class="o">.</span><span class="n">d0Cut</span> <span class="o">=</span> <span class="mf">9999.</span></div><div class='line' id='LC197'><span class="n">process</span><span class="o">.</span><span class="n">pfMuonsFromVertex</span><span class="o">.</span><span class="n">d0SigCut</span> <span class="o">=</span> <span class="mf">9999.</span></div><div class='line' id='LC198'><span class="n">process</span><span class="o">.</span><span class="n">pfMuonsFromVertex</span><span class="o">.</span><span class="n">dzCut</span> <span class="o">=</span> <span class="mf">9999.</span></div><div class='line' id='LC199'><span class="n">process</span><span class="o">.</span><span class="n">pfMuonsFromVertex</span><span class="o">.</span><span class="n">dzSigCut</span> <span class="o">=</span> <span class="mf">9999.</span></div><div class='line' id='LC200'><br/></div><div class='line' id='LC201'><br/></div><div class='line' id='LC202'><br/></div><div class='line' id='LC203'><span class="c">### ========================</span></div><div class='line' id='LC204'><span class="c">### HERMETIC TOP PROJECTION</span></div><div class='line' id='LC205'><span class="c">### ========================</span></div><div class='line' id='LC206'><br/></div><div class='line' id='LC207'><span class="k">if</span><span class="p">(</span><span class="n">hermeticTopProjection</span><span class="p">):</span></div><div class='line' id='LC208'><br/></div><div class='line' id='LC209'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">### ELECTRONS</span></div><div class='line' id='LC210'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">pfSelectedElectrons</span><span class="o">.</span><span class="n">cut</span> <span class="o">=</span> <span class="s">&#39;abs(eta)&lt;2.5 &amp;&amp; gsfElectronRef.pt&gt;20. &amp;&amp; gsfTrackRef.isNonnull &#39;</span></div><div class='line' id='LC211'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC212'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s">&quot;EGamma.EGammaAnalysisTools.electronIsolatorFromEffectiveArea_cfi&quot;</span><span class="p">)</span></div><div class='line' id='LC213'><br/></div><div class='line' id='LC214'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">pfIsolatedElectrons</span><span class="o">.</span><span class="n">deltaBetaIsolationValueMap</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&#39;elPFIsoValueEA03&#39;</span><span class="p">)</span></div><div class='line' id='LC215'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">pfIsolatedElectrons</span><span class="o">.</span><span class="n">doDeltaBetaCorrection</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">pfIsolatedElectrons</span><span class="o">.</span><span class="n">deltaBetaFactor</span> <span class="o">=</span> <span class="o">-</span><span class="mf">1.0</span></div><div class='line' id='LC217'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">pfIsolatedElectrons</span><span class="o">.</span><span class="n">isolationCut</span> <span class="o">=</span> <span class="mf">0.15</span></div><div class='line' id='LC218'><br/></div><div class='line' id='LC219'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patPF2PATSequence</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span> <span class="n">process</span><span class="o">.</span><span class="n">pfSelectedElectrons</span><span class="p">,</span> <span class="n">process</span><span class="o">.</span><span class="n">patElectronIDs</span>  <span class="o">+</span> <span class="n">process</span><span class="o">.</span><span class="n">pfSelectedElectrons</span> <span class="o">+</span> <span class="n">process</span><span class="o">.</span><span class="n">elPFIsoValueEA03</span><span class="p">)</span></div><div class='line' id='LC220'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">###  same definition as for the veto electrons</span></div><div class='line' id='LC221'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">selectedPatElectrons</span><span class="o">.</span><span class="n">cut</span> <span class="o">=</span> <span class="s">&#39;&#39;&#39; isPF &amp;&amp; ecalDrivenMomentum.pt &gt; 20 &amp;&amp; abs(eta) &lt; 2.5 &amp;&amp; userFloat(</span><span class="se">\&quot;</span><span class="s">RhoCorrectedIso</span><span class="se">\&quot;</span><span class="s">) &lt;0.15&#39;&#39;&#39;</span></div><div class='line' id='LC222'><br/></div><div class='line' id='LC223'><br/></div><div class='line' id='LC224'><br/></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">### MUONS</span></div><div class='line' id='LC226'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">pfSelectedMuons</span><span class="o">.</span><span class="n">cut</span> <span class="o">=</span> <span class="s">&#39;abs(eta)&lt;2.5 &amp;&amp; pt&gt;10.&#39;</span></div><div class='line' id='LC227'><span class="c">#    process.pfSelectedMuons.cut = &#39;abs(eta)&lt;2.5 &amp;&amp; pt&gt;10. &amp;&amp; ( isGlobalMuon || isTrackerMuon )&#39;</span></div><div class='line' id='LC228'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">pfIsolatedMuons</span><span class="o">.</span><span class="n">doDeltaBetaCorrection</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC229'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">pfIsolatedMuons</span><span class="o">.</span><span class="n">deltaBetaFactor</span> <span class="o">=</span> <span class="o">-</span><span class="mf">0.5</span></div><div class='line' id='LC230'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">pfIsolatedMuons</span><span class="o">.</span><span class="n">isolationCut</span> <span class="o">=</span> <span class="mf">0.2</span></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC232'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patMuons</span><span class="o">.</span><span class="n">embedTrack</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC233'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#process.patMuons.usePV = False</span></div><div class='line' id='LC234'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">###  same definition as for the veto muons</span></div><div class='line' id='LC235'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">selectedPatMuons</span><span class="o">.</span><span class="n">cut</span> <span class="o">=</span> <span class="s">&#39;&#39;&#39;abs(eta)&lt;2.5 &amp;&amp; pt&gt;10. &amp;&amp;</span></div><div class='line' id='LC236'><span class="s">    (chargedHadronIso+max(0.,neutralHadronIso+photonIso-0.50*puChargedHadronIso))/pt &lt; 0.20 &amp;&amp;</span></div><div class='line' id='LC237'><span class="s">    (isPFMuon &amp;&amp; (isGlobalMuon || isTrackerMuon) )&#39;&#39;&#39;</span></div><div class='line' id='LC238'><br/></div><div class='line' id='LC239'><br/></div><div class='line' id='LC240'><br/></div><div class='line' id='LC241'><br/></div><div class='line' id='LC242'><span class="c"># Define the PAT sequence:</span></div><div class='line' id='LC243'><span class="n">process</span><span class="o">.</span><span class="n">patseq</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">Sequence</span><span class="p">(</span></div><div class='line' id='LC244'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">goodOfflinePrimaryVertices</span> <span class="o">*</span></div><div class='line' id='LC245'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patElectronIDs</span> <span class="o">*</span></div><div class='line' id='LC246'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">getattr</span><span class="p">(</span><span class="n">process</span><span class="p">,</span><span class="s">&quot;patPF2PATSequence&quot;</span><span class="o">+</span><span class="n">postfix</span><span class="p">)</span></div><div class='line' id='LC247'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC248'><br/></div><div class='line' id='LC249'><span class="c"># Add PUJetID</span></div><div class='line' id='LC250'><span class="n">process</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s">&quot;CMGTools.External.pujetidsequence_cff&quot;</span><span class="p">)</span></div><div class='line' id='LC251'><br/></div><div class='line' id='LC252'><span class="c"># Define new PAT muons/electrons with no isolation in pf reco (ZeroIso suffix)</span></div><div class='line' id='LC253'><span class="c"># They will be used to get anti-isolated leptons:</span></div><div class='line' id='LC254'><br/></div><div class='line' id='LC255'><br/></div><div class='line' id='LC256'><span class="c"># MuonsZeroIso</span></div><div class='line' id='LC257'><span class="n">process</span><span class="o">.</span><span class="n">pfIsolatedMuonsZeroIso</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">pfIsolatedMuons</span><span class="o">.</span><span class="n">clone</span><span class="p">(</span><span class="n">combinedIsolationCut</span> <span class="o">=</span>  <span class="n">cms</span><span class="o">.</span><span class="n">double</span><span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="s">&quot;inf&quot;</span><span class="p">)),</span></div><div class='line' id='LC258'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">isolationCut</span> <span class="o">=</span>  <span class="n">cms</span><span class="o">.</span><span class="n">double</span><span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="s">&quot;inf&quot;</span><span class="p">))</span></div><div class='line' id='LC259'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC260'><span class="kn">from</span> <span class="nn">TopQuarkAnalysis.SingleTop.AdaptPFMuonsFix_cff</span> <span class="kn">import</span> <span class="n">adaptPFMuonsAnd</span></div><div class='line' id='LC261'><span class="n">process</span><span class="o">.</span><span class="n">patMuonsZeroIso</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">patMuons</span><span class="o">.</span><span class="n">clone</span><span class="p">(</span><span class="n">pfMuonSource</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;pfIsolatedMuonsZeroIso&quot;</span><span class="p">))</span></div><div class='line' id='LC262'><span class="c"># use pf isolation, but do not change matching:</span></div><div class='line' id='LC263'><span class="n">tmp</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">muonMatch</span><span class="o">.</span><span class="n">src</span></div><div class='line' id='LC264'><br/></div><div class='line' id='LC265'><span class="n">adaptPFMuonsAnd</span><span class="p">(</span><span class="n">process</span><span class="p">,</span> <span class="n">process</span><span class="o">.</span><span class="n">patMuonsZeroIso</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">)</span></div><div class='line' id='LC266'><span class="n">process</span><span class="o">.</span><span class="n">muonMatch</span><span class="o">.</span><span class="n">src</span> <span class="o">=</span> <span class="n">tmp</span></div><div class='line' id='LC267'><span class="n">process</span><span class="o">.</span><span class="n">muonMatchZeroIso</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">muonMatch</span><span class="o">.</span><span class="n">clone</span><span class="p">(</span><span class="n">src</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;pfIsolatedMuonsZeroIso&quot;</span><span class="p">))</span></div><div class='line' id='LC268'><span class="n">process</span><span class="o">.</span><span class="n">patMuonsZeroIso</span><span class="o">.</span><span class="n">genParticleMatch</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;muonMatchZeroIso&quot;</span><span class="p">)</span></div><div class='line' id='LC269'><span class="n">process</span><span class="o">.</span><span class="n">patMuonsZeroIso</span><span class="o">.</span><span class="n">pfMuonSource</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;pfIsolatedMuonsZeroIso&quot;</span><span class="p">)</span></div><div class='line' id='LC270'><br/></div><div class='line' id='LC271'><br/></div><div class='line' id='LC272'><span class="c"># ElectronsZeroIso</span></div><div class='line' id='LC273'><span class="n">process</span><span class="o">.</span><span class="n">pfIsolatedElectronsZeroIso</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">pfIsolatedElectrons</span><span class="o">.</span><span class="n">clone</span><span class="p">(</span><span class="n">combinedIsolationCut</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">double</span><span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="s">&quot;inf&quot;</span><span class="p">)),</span></div><div class='line' id='LC274'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">isolationCut</span> <span class="o">=</span>  <span class="n">cms</span><span class="o">.</span><span class="n">double</span><span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="s">&quot;inf&quot;</span><span class="p">)),</span></div><div class='line' id='LC275'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC276'><span class="n">process</span><span class="o">.</span><span class="n">patElectronsZeroIso</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">patElectrons</span><span class="o">.</span><span class="n">clone</span><span class="p">(</span><span class="n">pfElectronSource</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;pfIsolatedElectronsZeroIso&quot;</span><span class="p">))</span></div><div class='line' id='LC277'><br/></div><div class='line' id='LC278'><span class="c">#Define ZeroIso leptons sequence:</span></div><div class='line' id='LC279'><span class="k">if</span> <span class="n">isData</span><span class="p">:</span></div><div class='line' id='LC280'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">ZeroIsoLeptonSequence</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">Sequence</span><span class="p">(</span></div><div class='line' id='LC281'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">pfIsolatedMuonsZeroIso</span> <span class="o">+</span></div><div class='line' id='LC282'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patMuonsZeroIso</span> <span class="o">+</span></div><div class='line' id='LC283'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">pfIsolatedElectronsZeroIso</span> <span class="o">+</span></div><div class='line' id='LC284'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patElectronsZeroIso</span></div><div class='line' id='LC285'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC286'><span class="k">else</span><span class="p">:</span>    </div><div class='line' id='LC287'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">ZeroIsoLeptonSequence</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">Sequence</span><span class="p">(</span></div><div class='line' id='LC288'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">pfIsolatedMuonsZeroIso</span> <span class="o">+</span></div><div class='line' id='LC289'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">muonMatchZeroIso</span> <span class="o">+</span></div><div class='line' id='LC290'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patMuonsZeroIso</span> <span class="o">+</span></div><div class='line' id='LC291'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">pfIsolatedElectronsZeroIso</span> <span class="o">+</span></div><div class='line' id='LC292'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patElectronsZeroIso</span></div><div class='line' id='LC293'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC294'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC295'><span class="c">##### Define leptons collections useful in single top analysis</span></div><div class='line' id='LC296'><br/></div><div class='line' id='LC297'><span class="c"># Veto leptons</span></div><div class='line' id='LC298'><span class="n">process</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s">&quot;TopQuarkAnalysis.SingleTop.userDataLeptonProducers_cfi&quot;</span><span class="p">)</span> </div><div class='line' id='LC299'><br/></div><div class='line' id='LC300'><span class="n">process</span><span class="o">.</span><span class="n">vetoMuons</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">userDataMuons</span><span class="o">.</span><span class="n">clone</span><span class="p">(</span></div><div class='line' id='LC301'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cut</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&quot; (isGlobalMuon || isTrackerMuon) &quot;</span> <span class="o">+</span></div><div class='line' id='LC302'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp; pt &gt; 10 &amp; abs(eta) &lt; 2.5 &quot;</span> <span class="o">+</span></div><div class='line' id='LC303'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp; userFloat(</span><span class="se">\&quot;</span><span class="s">DeltaCorrectedIso</span><span class="se">\&quot;</span><span class="s">) &lt;0.2 &quot;</span><span class="p">)</span></div><div class='line' id='LC304'><span class="p">)</span></div><div class='line' id='LC305'><br/></div><div class='line' id='LC306'><span class="n">process</span><span class="o">.</span><span class="n">vetoElectrons</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">userDataElectrons</span><span class="o">.</span><span class="n">clone</span><span class="p">(</span></div><div class='line' id='LC307'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cut</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&quot;ecalDrivenMomentum.pt &gt; 20 &quot;</span> <span class="o">+</span></div><div class='line' id='LC308'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp; abs(eta) &lt; 2.5 &quot;</span> <span class="o">+</span></div><div class='line' id='LC309'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp; userFloat(</span><span class="se">\&quot;</span><span class="s">RhoCorrectedIso</span><span class="se">\&quot;</span><span class="s">) &lt;0.15&quot;</span><span class="p">)</span><span class="c"># +</span></div><div class='line' id='LC310'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># &quot;&amp; userFloat(\&quot;PassesVetoID\&quot;) &gt;0.0&quot;)</span></div><div class='line' id='LC311'><span class="p">)</span></div><div class='line' id='LC312'><br/></div><div class='line' id='LC313'><span class="n">process</span><span class="o">.</span><span class="n">vetoElectronsMVA</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">userDataElectrons</span><span class="o">.</span><span class="n">clone</span><span class="p">(</span></div><div class='line' id='LC314'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cut</span> <span class="o">=</span>  <span class="n">cms</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&quot; ecalDrivenMomentum.pt &gt; 20&quot;</span> <span class="o">+</span></div><div class='line' id='LC315'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp; abs(eta) &lt; 2.5 &amp;&amp; userFloat(</span><span class="se">\&quot;</span><span class="s">RhoCorrectedIso</span><span class="se">\&quot;</span><span class="s">) &lt;0.15&quot;</span><span class="p">)</span><span class="c"># +</span></div><div class='line' id='LC316'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#  &quot;&amp; electronID(&#39;mvaTrigV0&#39;) &gt;0.0&quot;)</span></div><div class='line' id='LC317'><span class="p">)</span></div><div class='line' id='LC318'><br/></div><div class='line' id='LC319'><span class="c"># Tight leptons</span></div><div class='line' id='LC320'><span class="n">process</span><span class="o">.</span><span class="n">tightMuons</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">userDataMuons</span><span class="o">.</span><span class="n">clone</span><span class="p">(</span></div><div class='line' id='LC321'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cut</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&quot; pt &gt; 26 &amp; isGlobalMuon &amp;&amp; isPFMuon &amp; abs(eta) &lt; 2.1 &amp;&amp; normChi2 &lt; 10 &amp;&amp; track.hitPattern.trackerLayersWithMeasurement&gt;5 &quot;</span><span class="o">+</span></div><div class='line' id='LC322'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp; numberOfMatchedStations() &gt; 1 &amp;&amp; innerTrack.hitPattern.numberOfValidPixelHits &gt; 0 &quot;</span> <span class="o">+</span></div><div class='line' id='LC323'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp; globalTrack.hitPattern.numberOfValidMuonHits &gt; 0&quot;</span> <span class="o">+</span></div><div class='line' id='LC324'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#                     &quot;&amp; userFloat(&#39;VertexDxy&#39;)&lt;0.02&quot; +</span></div><div class='line' id='LC325'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp; abs(dB) &lt; 0.2&quot;</span></div><div class='line' id='LC326'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp; userFloat(&#39;VertexDz&#39;)&lt;0.5&quot;</span> <span class="o">+</span></div><div class='line' id='LC327'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp; userFloat(</span><span class="se">\&quot;</span><span class="s">DeltaCorrectedIso</span><span class="se">\&quot;</span><span class="s">) &lt;0.12 &quot;</span> <span class="p">)</span></div><div class='line' id='LC328'><span class="p">)</span></div><div class='line' id='LC329'><br/></div><div class='line' id='LC330'><span class="n">process</span><span class="o">.</span><span class="n">tightElectrons</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">userDataElectrons</span><span class="o">.</span><span class="n">clone</span><span class="p">(</span></div><div class='line' id='LC331'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cut</span> <span class="o">=</span>  <span class="n">cms</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&quot; ecalDrivenMomentum.pt &gt; 30  &amp;&amp; abs(eta)&lt;2.5&quot;</span> <span class="o">+</span></div><div class='line' id='LC332'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp; ( abs(superCluster.eta)&gt; 1.5660 || abs(superCluster.eta)&lt;1.4442)&quot;</span> <span class="o">+</span></div><div class='line' id='LC333'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp; gsfTrack.trackerExpectedHitsInner.numberOfHits &lt;=0&quot;</span> <span class="o">+</span></div><div class='line' id='LC334'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp; passConversionVeto&quot;</span> <span class="o">+</span></div><div class='line' id='LC335'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;&amp; userFloat(&#39;VertexDxy&#39;)&lt;0.02&quot; +</span></div><div class='line' id='LC336'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp; userFloat(&#39;RhoCorrectedIso&#39;)&lt;0.1&quot;</span> <span class="p">)</span></div><div class='line' id='LC337'><span class="p">)</span></div><div class='line' id='LC338'><br/></div><div class='line' id='LC339'><span class="c"># Tight leptons ZeroIso</span></div><div class='line' id='LC340'><span class="n">process</span><span class="o">.</span><span class="n">tightMuonsZeroIso</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">userDataMuons</span><span class="o">.</span><span class="n">clone</span><span class="p">(</span></div><div class='line' id='LC341'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">src</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;patMuonsZeroIso&quot;</span><span class="p">),</span></div><div class='line' id='LC342'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cut</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&quot; pt &gt; 26 &amp; isGlobalMuon &amp;&amp; isPFMuon &amp; abs(eta) &lt; 2.1 &amp;&amp; normChi2 &lt; 10 &amp;&amp; track.hitPattern.trackerLayersWithMeasurement&gt;5 &quot;</span><span class="o">+</span></div><div class='line' id='LC343'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp; numberOfMatchedStations() &gt; 1 &amp;&amp; innerTrack.hitPattern.numberOfValidPixelHits &gt; 0 &quot;</span> <span class="o">+</span></div><div class='line' id='LC344'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp; globalTrack.hitPattern.numberOfValidMuonHits &gt; 0&quot;</span><span class="p">)</span></div><div class='line' id='LC345'><span class="p">)</span></div><div class='line' id='LC346'><br/></div><div class='line' id='LC347'><span class="n">process</span><span class="o">.</span><span class="n">tightElectronsZeroIso</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">userDataElectrons</span><span class="o">.</span><span class="n">clone</span><span class="p">(</span></div><div class='line' id='LC348'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">src</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;patElectronsZeroIso&quot;</span><span class="p">),</span></div><div class='line' id='LC349'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cut</span> <span class="o">=</span>  <span class="n">cms</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&quot; ecalDrivenMomentum.pt &gt; 30  &amp;&amp; abs(eta)&lt;2.5&quot;</span> <span class="o">+</span></div><div class='line' id='LC350'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp; ( abs(superCluster.eta)&gt; 1.5660 || abs(superCluster.eta)&lt;1.4442)&quot;</span> <span class="o">+</span></div><div class='line' id='LC351'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp; passConversionVeto&quot;</span><span class="p">)</span></div><div class='line' id='LC352'><span class="p">)</span></div><div class='line' id='LC353'><br/></div><div class='line' id='LC354'><span class="c">##### Filtering on leptons numbers</span></div><div class='line' id='LC355'><span class="n">process</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s">&quot;TopQuarkAnalysis.SingleTop.leptonCounterFilter_cfi&quot;</span><span class="p">)</span> </div><div class='line' id='LC356'><span class="c"># Select events with at least 1 tight lepton OR at least one tight leptonNoIso</span></div><div class='line' id='LC357'><span class="n">process</span><span class="o">.</span><span class="n">countLeptons</span><span class="o">.</span><span class="n">minNumberLoose</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC358'><span class="n">process</span><span class="o">.</span><span class="n">countLeptons</span><span class="o">.</span><span class="n">maxNumberLoose</span> <span class="o">=</span> <span class="mi">99</span></div><div class='line' id='LC359'><span class="n">process</span><span class="o">.</span><span class="n">countLeptons</span><span class="o">.</span><span class="n">minNumberTight</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC360'><span class="n">process</span><span class="o">.</span><span class="n">countLeptons</span><span class="o">.</span><span class="n">maxNumberTight</span> <span class="o">=</span> <span class="mi">99</span></div><div class='line' id='LC361'><span class="n">process</span><span class="o">.</span><span class="n">countLeptons</span><span class="o">.</span><span class="n">minNumberQCD</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC362'><span class="n">process</span><span class="o">.</span><span class="n">countLeptons</span><span class="o">.</span><span class="n">maxNumberQCD</span> <span class="o">=</span> <span class="mi">99</span></div><div class='line' id='LC363'><br/></div><div class='line' id='LC364'><span class="c"># define Jets for single top analysis</span></div><div class='line' id='LC365'><span class="n">process</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s">&quot;TopQuarkAnalysis.SingleTop.userDataJetsProducer_cfi&quot;</span><span class="p">)</span> </div><div class='line' id='LC366'><br/></div><div class='line' id='LC367'><span class="n">process</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s">&quot;TopQuarkAnalysis.SingleTop.userDataMETsProducer_cfi&quot;</span><span class="p">)</span> </div><div class='line' id='LC368'><br/></div><div class='line' id='LC369'><span class="c">#definition: Jets Loose</span></div><div class='line' id='LC370'><span class="n">process</span><span class="o">.</span><span class="n">topJetsPF</span><span class="o">.</span><span class="n">cut</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&quot;numberOfDaughters()&gt;1 &amp; pt()&gt; 20 &amp;&amp; abs(eta())&lt;4.7 &quot;</span> <span class="o">+</span></div><div class='line' id='LC371'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot; &amp; ((abs(eta())&gt;=2.4) || ( chargedHadronEnergyFraction() &gt; 0 &amp; chargedMultiplicity()&gt;0 &quot;</span> <span class="o">+</span></div><div class='line' id='LC372'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot; &amp; chargedEmEnergyFraction()&lt;0.99))&quot;</span> <span class="o">+</span></div><div class='line' id='LC373'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot; &amp; (neutralHadronEnergy + HFHadronEnergy) / energy &lt; 0.99&quot;</span> <span class="p">)</span></div><div class='line' id='LC374'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#neutralEmEnergyFraction() &lt; 0.99 &amp; neutralHadronEnergyFraction() &lt; 0.99 &quot;)</span></div><div class='line' id='LC375'><br/></div><div class='line' id='LC376'><span class="n">process</span><span class="o">.</span><span class="n">UnclusteredMETPF</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">EDProducer</span><span class="p">(</span><span class="s">&quot;SingleTopUnclusteredMETProducer&quot;</span><span class="p">,</span></div><div class='line' id='LC377'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">metSource</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;patType1CorrectedPFMet&quot;</span><span class="p">),</span></div><div class='line' id='LC378'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">jetsSource</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;selectedPatJets&quot;</span><span class="p">),</span></div><div class='line' id='LC379'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">electronsSource</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;selectedPatElectrons&quot;</span><span class="p">),</span></div><div class='line' id='LC380'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">muonsSource</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;selectedPatMuons&quot;</span><span class="p">),</span></div><div class='line' id='LC381'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC382'><br/></div><div class='line' id='LC383'><br/></div><div class='line' id='LC384'><span class="n">process</span><span class="o">.</span><span class="n">topJetsPF</span><span class="o">.</span><span class="n">isData</span> <span class="o">=</span> <span class="n">isData</span></div><div class='line' id='LC385'><span class="n">process</span><span class="o">.</span><span class="n">topMETsPF</span><span class="o">.</span><span class="n">isData</span> <span class="o">=</span> <span class="n">isData</span></div><div class='line' id='LC386'><span class="n">process</span><span class="o">.</span><span class="n">topMETsPF</span><span class="o">.</span><span class="n">addExternalUnclusteredMET</span> <span class="o">=</span> <span class="n">doRunMETUncertainties</span></div><div class='line' id='LC387'><span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">doRunMETUncertainties</span><span class="p">):</span> </div><div class='line' id='LC388'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">topMETsPF</span><span class="o">.</span><span class="n">metsSrc</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;patMETs&quot;</span><span class="p">)</span></div><div class='line' id='LC389'><br/></div><div class='line' id='LC390'><span class="k">if</span> <span class="n">isData</span><span class="p">:</span></div><div class='line' id='LC391'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">basePath</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">Sequence</span><span class="p">(</span></div><div class='line' id='LC392'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">vetoMuons</span> <span class="o">+</span></div><div class='line' id='LC393'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">vetoElectrons</span> <span class="o">+</span></div><div class='line' id='LC394'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">vetoElectronsMVA</span> <span class="o">+</span></div><div class='line' id='LC395'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">topJetsPF</span> <span class="o">+</span></div><div class='line' id='LC396'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">topMETsPF</span> <span class="o">+</span></div><div class='line' id='LC397'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">tightMuonsZeroIso</span> <span class="o">+</span></div><div class='line' id='LC398'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">tightElectronsZeroIso</span> <span class="o">+</span></div><div class='line' id='LC399'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">tightMuons</span> <span class="o">+</span></div><div class='line' id='LC400'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">tightElectrons</span></div><div class='line' id='LC401'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC402'><br/></div><div class='line' id='LC403'><span class="k">else</span><span class="p">:</span>    </div><div class='line' id='LC404'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">basePath</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">Sequence</span><span class="p">(</span></div><div class='line' id='LC405'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">vetoMuons</span> <span class="o">+</span></div><div class='line' id='LC406'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">vetoElectrons</span> <span class="o">+</span></div><div class='line' id='LC407'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">vetoElectronsMVA</span> <span class="o">+</span></div><div class='line' id='LC408'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">topJetsPF</span> <span class="o">+</span></div><div class='line' id='LC409'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">topMETsPF</span> <span class="o">+</span></div><div class='line' id='LC410'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">UnclusteredMETPF</span> <span class="o">+</span></div><div class='line' id='LC411'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">tightMuonsZeroIso</span> <span class="o">+</span></div><div class='line' id='LC412'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">tightElectronsZeroIso</span> <span class="o">+</span></div><div class='line' id='LC413'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">tightMuons</span> <span class="o">+</span></div><div class='line' id='LC414'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">tightElectrons</span></div><div class='line' id='LC415'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC416'><br/></div><div class='line' id='LC417'><span class="c">#Trigger filter to be eventually used:</span></div><div class='line' id='LC418'><span class="kn">import</span> <span class="nn">HLTrigger.HLTfilters.triggerResultsFilter_cfi</span> <span class="kn">as</span> <span class="nn">triggerFilter</span></div><div class='line' id='LC419'><br/></div><div class='line' id='LC420'><span class="n">process</span><span class="o">.</span><span class="n">HLTFilterMu2012</span>  <span class="o">=</span> <span class="n">triggerFilter</span><span class="o">.</span><span class="n">triggerResultsFilter</span><span class="o">.</span><span class="n">clone</span><span class="p">(</span></div><div class='line' id='LC421'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">hltResults</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span> <span class="s">&quot;TriggerResults&quot;</span><span class="p">,</span><span class="s">&quot;&quot;</span><span class="p">,</span><span class="s">&quot;HLT&quot;</span> <span class="p">),</span></div><div class='line' id='LC422'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">triggerConditions</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;HLT_*&quot;</span><span class="p">],</span><span class="c">#All trigger paths are included in the skim</span></div><div class='line' id='LC423'><span class="c">#    triggerConditions = [&quot;HLT_IsoMu24_eta2p1_v*&quot;],</span></div><div class='line' id='LC424'><span class="c">#    triggerConditions = [&quot;HLT_Ele27_WP80_v*&quot;],</span></div><div class='line' id='LC425'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">l1tResults</span> <span class="o">=</span> <span class="s">&#39;&#39;</span><span class="p">,</span></div><div class='line' id='LC426'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">throw</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC427'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC428'><br/></div><div class='line' id='LC429'><span class="kn">from</span> <span class="nn">PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi</span> <span class="kn">import</span> <span class="o">*</span></div><div class='line' id='LC430'><span class="n">process</span><span class="o">.</span><span class="n">jetsCut</span> <span class="o">=</span> <span class="n">countPatJets</span><span class="o">.</span><span class="n">clone</span><span class="p">(</span><span class="n">src</span> <span class="o">=</span> <span class="s">&#39;topJetsPF&#39;</span><span class="p">,</span> <span class="n">minNumber</span> <span class="o">=</span> <span class="mi">2</span><span class="p">)</span></div><div class='line' id='LC431'><br/></div><div class='line' id='LC432'><span class="c"># Overall skim path</span></div><div class='line' id='LC433'><span class="n">process</span><span class="o">.</span><span class="n">singleTopSkimPath</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">Path</span><span class="p">(</span></div><div class='line' id='LC434'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">HLTFilterMu2012</span> <span class="o">*</span></div><div class='line' id='LC435'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">patseq</span> <span class="o">+</span></div><div class='line' id='LC436'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">puJetIdSqeuence</span> <span class="o">+</span></div><div class='line' id='LC437'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">puJetIdSqeuenceChs</span> <span class="o">*</span></div><div class='line' id='LC438'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">ZeroIsoLeptonSequence</span> <span class="o">*</span></div><div class='line' id='LC439'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">basePath</span> <span class="c">#+</span></div><div class='line' id='LC440'><span class="c"># moved preselection in a standalone path</span></div><div class='line' id='LC441'><span class="c">#    process.preselection# + </span></div><div class='line' id='LC442'><span class="c">#    process.nTuplesSkim </span></div><div class='line' id='LC443'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC444'><br/></div><div class='line' id='LC445'><span class="c"># Load recommended event filters</span></div><div class='line' id='LC446'><span class="n">process</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s">&quot;TopQuarkAnalysis.SingleTop.SingleTopEventFilters_cff&quot;</span><span class="p">)</span> </div><div class='line' id='LC447'><br/></div><div class='line' id='LC448'><span class="c"># Define event filtering path</span></div><div class='line' id='LC449'><span class="c">#process.preselection = cms.Sequence(</span></div><div class='line' id='LC450'><span class="n">process</span><span class="o">.</span><span class="n">preselection</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">Path</span><span class="p">(</span></div><div class='line' id='LC451'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">HLTFilterMu2012</span> <span class="o">*</span></div><div class='line' id='LC452'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">HBHENoiseFilter</span> <span class="o">*</span></div><div class='line' id='LC453'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">scrapingVeto</span> <span class="o">*</span></div><div class='line' id='LC454'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">CSCTightHaloFilter</span> <span class="o">*</span></div><div class='line' id='LC455'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">hcalLaserEventFilter</span> <span class="o">*</span></div><div class='line' id='LC456'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">EcalDeadCellTriggerPrimitiveFilter</span> <span class="o">*</span></div><div class='line' id='LC457'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">EcalDeadCellBoundaryEnergyFilter</span> <span class="o">*</span></div><div class='line' id='LC458'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">goodVertices</span> <span class="o">*</span></div><div class='line' id='LC459'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">trackingFailureFilter</span> <span class="o">*</span></div><div class='line' id='LC460'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">eeBadScFilter</span> <span class="o">*</span></div><div class='line' id='LC461'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">ecalLaserCorrFilter</span> <span class="o">*</span></div><div class='line' id='LC462'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="o">~</span><span class="n">process</span><span class="o">.</span><span class="n">manystripclus53X</span> <span class="o">*</span></div><div class='line' id='LC463'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="o">~</span><span class="n">process</span><span class="o">.</span><span class="n">toomanystripclus53X</span> <span class="o">*</span></div><div class='line' id='LC464'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="o">~</span><span class="n">process</span><span class="o">.</span><span class="n">logErrorTooManyClusters</span> <span class="o">*</span></div><div class='line' id='LC465'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">countLeptons</span></div><div class='line' id='LC466'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC467'><br/></div><div class='line' id='LC468'><span class="k">if</span> <span class="n">addJetsCut</span><span class="p">:</span></div><div class='line' id='LC469'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">preselection</span> <span class="o">+=</span> <span class="n">process</span><span class="o">.</span><span class="n">jetsCut</span></div><div class='line' id='LC470'><br/></div><div class='line' id='LC471'><span class="n">process</span><span class="o">.</span><span class="n">fullPath</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">Schedule</span><span class="p">(</span></div><div class='line' id='LC472'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">singleTopSkimPath</span><span class="p">,</span></div><div class='line' id='LC473'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">preselection</span></div><div class='line' id='LC474'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC475'><br/></div><div class='line' id='LC476'><span class="c">#Objects included in the pat-tuples</span></div><div class='line' id='LC477'><span class="n">savePatTupleSkimLoose</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">untracked</span><span class="o">.</span><span class="n">vstring</span><span class="p">(</span></div><div class='line' id='LC478'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;drop *&#39;</span><span class="p">,</span></div><div class='line' id='LC479'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep *_*Muons_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC480'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep *_pfMuonsFromVertex_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC481'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep patMuons_selectedPatMuons_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC482'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep patElectrons_selectedPatElectrons_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC483'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep patJets_selectedPatJets_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC484'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep *_selectedPatJets_genJets_*&#39;</span><span class="p">,</span> <span class="c"># to get embedded genJets</span></div><div class='line' id='LC485'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep patMETs_patMETs_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC486'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep *_kt6PFJets_rho_*&#39;</span><span class="p">,</span></div><div class='line' id='LC487'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep *_topJetsPF_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC488'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep *_topMETsPF_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC489'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep patMuons_vetoMuons_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC490'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep *_vetoElectrons_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC491'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep *_vetoElectronsMVA_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC492'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep patMuons_tightMuons_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC493'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep *_tightElectrons_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC494'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep *_tightElectronsZeroIso_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC495'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep *_tightMuonsZeroIso_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC496'><span class="c"># vertex</span></div><div class='line' id='LC497'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep *_offlineBeamSpot_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC498'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep *_offlinePrimaryVertices_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC499'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep *_goodOfflinePrimaryVertices_*_*&#39;</span><span class="p">,</span> <span class="c"># needed by SingleTopVertexInfoDumper module</span></div><div class='line' id='LC500'><span class="c"># Trigger results</span></div><div class='line' id='LC501'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;keep *_TriggerResults_*_*&quot;</span><span class="p">,</span></div><div class='line' id='LC502'><span class="c"># gen particles</span></div><div class='line' id='LC503'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep *_genParticles_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC504'><span class="c"># gen info</span></div><div class='line' id='LC505'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep PileupSummaryInfos_*_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC506'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep GenEventInfoProduct_*_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC507'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep GenRunInfoProduct_*_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC508'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep LHEEventProduct_*_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC509'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep *_genEventScale_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC510'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;keep *_PDFInfo_*_*&#39;</span><span class="p">,</span></div><div class='line' id='LC511'><span class="p">)</span></div><div class='line' id='LC512'><br/></div><div class='line' id='LC513'><br/></div><div class='line' id='LC514'><span class="n">process</span><span class="o">.</span><span class="n">singleTopPatTuple</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">OutputModule</span><span class="p">(</span></div><div class='line' id='LC515'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;PoolOutputModule&quot;</span><span class="p">,</span></div><div class='line' id='LC516'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fileName</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">untracked</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&#39;singleTopSkim_&#39;</span><span class="o">+</span><span class="n">ChannelName</span><span class="o">+</span><span class="s">&#39;.root&#39;</span><span class="p">),</span></div><div class='line' id='LC517'><span class="c">#    SelectEvents   = cms.untracked.PSet(</span></div><div class='line' id='LC518'><span class="c">#      SelectEvents = cms.vstring(</span></div><div class='line' id='LC519'><span class="c">#        &#39;preselection&#39;)</span></div><div class='line' id='LC520'><span class="c">#        &#39;pathSelection&#39;)</span></div><div class='line' id='LC521'><span class="c">#      ),</span></div><div class='line' id='LC522'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">outputCommands</span> <span class="o">=</span> <span class="n">savePatTupleSkimLoose</span></div><div class='line' id='LC523'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC524'><span class="n">process</span><span class="o">.</span><span class="n">singleTopPatTuple</span><span class="o">.</span><span class="n">dropMetaData</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">untracked</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&quot;DROPPED&quot;</span><span class="p">)</span></div><div class='line' id='LC525'><br/></div><div class='line' id='LC526'><br/></div><div class='line' id='LC527'><span class="c">#### Ntuplization step ###</span></div><div class='line' id='LC528'><span class="c">########################################################</span></div><div class='line' id='LC529'><span class="n">process</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s">&quot;PhysicsTools.HepMCCandAlgos.flavorHistoryPaths_cfi&quot;</span><span class="p">)</span></div><div class='line' id='LC530'><span class="c">########################################################</span></div><div class='line' id='LC531'><br/></div><div class='line' id='LC532'><span class="c">######### GET generator info ##############</span></div><div class='line' id='LC533'><span class="c">#genJets:</span></div><div class='line' id='LC534'><span class="n">process</span><span class="o">.</span><span class="n">genJetsPF</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">EDProducer</span><span class="p">(</span></div><div class='line' id='LC535'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;SingleTopGenJetPtEtaProducer&quot;</span><span class="p">,</span></div><div class='line' id='LC536'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">jetsSource</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;topJetsPF&quot;</span><span class="p">),</span></div><div class='line' id='LC537'><span class="p">)</span></div><div class='line' id='LC538'><span class="c">#genAllJets:</span></div><div class='line' id='LC539'><span class="n">process</span><span class="o">.</span><span class="n">genAllJetsPF</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">EDProducer</span><span class="p">(</span></div><div class='line' id='LC540'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;SingleTopGenJetPtEtaProducer&quot;</span><span class="p">,</span></div><div class='line' id='LC541'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">jetsSource</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;selectedPatJets&quot;</span><span class="p">),</span></div><div class='line' id='LC542'><span class="p">)</span></div><div class='line' id='LC543'><span class="c">#PU Info</span></div><div class='line' id='LC544'><span class="n">process</span><span class="o">.</span><span class="n">NVertices</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">EDProducer</span><span class="p">(</span><span class="s">&quot;SingleTopPileUpProducer&quot;</span><span class="p">)</span></div><div class='line' id='LC545'><br/></div><div class='line' id='LC546'><span class="c">#n gen particles Info</span></div><div class='line' id='LC547'><span class="n">process</span><span class="o">.</span><span class="n">NGenParticles</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">EDProducer</span><span class="p">(</span><span class="s">&quot;SingleTopNGenParticlesProducer&quot;</span><span class="p">)</span></div><div class='line' id='LC548'><br/></div><div class='line' id='LC549'><span class="c">#PDF Info</span></div><div class='line' id='LC550'><span class="n">process</span><span class="o">.</span><span class="n">PDFInfo</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">EDProducer</span><span class="p">(</span> <span class="s">&quot;PDFInfoDumper&quot;</span> <span class="p">)</span></div><div class='line' id='LC551'><br/></div><div class='line' id='LC552'><span class="c">#Part of MC Truth particles production</span></div><div class='line' id='LC553'><span class="n">process</span><span class="o">.</span><span class="n">MCTruthParticles</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">EDProducer</span><span class="p">(</span></div><div class='line' id='LC554'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;SingleTopMCProducer&quot;</span><span class="p">,</span></div><div class='line' id='LC555'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">genParticlesSource</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">InputTag</span><span class="p">(</span><span class="s">&quot;genParticles&quot;</span><span class="p">)</span></div><div class='line' id='LC556'><span class="p">)</span></div><div class='line' id='LC557'><span class="c">#############################################</span></div><div class='line' id='LC558'><br/></div><div class='line' id='LC559'><span class="c">######### EdmNtuples production ##############</span></div><div class='line' id='LC560'><span class="n">process</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s">&quot;TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff&quot;</span><span class="p">)</span></div><div class='line' id='LC561'><br/></div><div class='line' id='LC562'><span class="c"># Ntuple sequence</span></div><div class='line' id='LC563'><span class="n">process</span><span class="o">.</span><span class="n">genPath</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">Sequence</span><span class="p">(</span></div><div class='line' id='LC564'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">genJetsPF</span> <span class="o">+</span></div><div class='line' id='LC565'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">genAllJetsPF</span> <span class="o">+</span></div><div class='line' id='LC566'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">NVertices</span> <span class="o">+</span></div><div class='line' id='LC567'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">NGenParticles</span> <span class="o">+</span></div><div class='line' id='LC568'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">PDFInfo</span>           </div><div class='line' id='LC569'><span class="p">)</span></div><div class='line' id='LC570'><br/></div><div class='line' id='LC571'><span class="n">process</span><span class="o">.</span><span class="n">singleTopNtuplePath</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">Sequence</span><span class="p">(</span></div><div class='line' id='LC572'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">nTuplesSkim</span> </div><div class='line' id='LC573'><span class="p">)</span></div><div class='line' id='LC574'><br/></div><div class='line' id='LC575'><span class="n">process</span><span class="o">.</span><span class="n">singleTopSkimPath</span> <span class="o">+=</span> <span class="n">process</span><span class="o">.</span><span class="n">singleTopNtuplePath</span></div><div class='line' id='LC576'><span class="k">if</span> <span class="ow">not</span><span class="p">(</span><span class="n">isData</span><span class="p">):</span> <span class="n">process</span><span class="o">.</span><span class="n">singleTopSkimPath</span> <span class="o">+=</span> <span class="n">process</span><span class="o">.</span><span class="n">genPath</span></div><div class='line' id='LC577'><br/></div><div class='line' id='LC578'><span class="kn">from</span> <span class="nn">TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff</span> <span class="kn">import</span> <span class="n">saveNTuplesSkimLoose</span></div><div class='line' id='LC579'><br/></div><div class='line' id='LC580'><span class="c">#Add MC Truth information:</span></div><div class='line' id='LC581'><span class="n">doMCTruth</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC582'><span class="k">if</span> <span class="n">isData</span><span class="p">:</span></div><div class='line' id='LC583'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">doMCTruth</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC584'><br/></div><div class='line' id='LC585'><span class="k">if</span> <span class="n">doMCTruth</span><span class="p">:</span></div><div class='line' id='LC586'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">MCTruth</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">Sequence</span><span class="p">(</span></div><div class='line' id='LC587'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">MCTruthParticles</span> <span class="o">+</span></div><div class='line' id='LC588'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">nTuplesSkimMCTruth</span></div><div class='line' id='LC589'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC590'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">singleTopSkimPath</span> <span class="o">+=</span> <span class="n">process</span><span class="o">.</span><span class="n">MCTruth</span></div><div class='line' id='LC591'><br/></div><div class='line' id='LC592'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">saveNTuplesSkimLoose</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;keep  floats_MCTruthParticles_*_*&#39;</span><span class="p">)</span></div><div class='line' id='LC593'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">saveNTuplesSkimLoose</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;keep  ints_MCTruthParticles_*_*&#39;</span><span class="p">)</span></div><div class='line' id='LC594'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">saveNTuplesSkimLoose</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;keep  floats_singleTopMCLeptons_*_*&#39;</span><span class="p">)</span></div><div class='line' id='LC595'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">saveNTuplesSkimLoose</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;keep  floats_singleTopMCQuarks_*_*&#39;</span><span class="p">)</span></div><div class='line' id='LC596'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">saveNTuplesSkimLoose</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;keep  floats_singleTopMCNeutrinos_*_*&#39;</span><span class="p">)</span></div><div class='line' id='LC597'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">saveNTuplesSkimLoose</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;keep  floats_singleTopMCBQuarks_*_*&#39;</span><span class="p">)</span></div><div class='line' id='LC598'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">saveNTuplesSkimLoose</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;keep  floats_singleTopMCTops_*_*&#39;</span><span class="p">)</span></div><div class='line' id='LC599'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">saveNTuplesSkimLoose</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;keep  floats_singleTopMCTopsW_*_*&#39;</span><span class="p">)</span></div><div class='line' id='LC600'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">saveNTuplesSkimLoose</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;keep  floats_singleTopMCTopsBQuark_*_*&#39;</span><span class="p">)</span></div><div class='line' id='LC601'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">saveNTuplesSkimLoose</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;keep  floats_singleTopMCTopsLepton_*_*&#39;</span><span class="p">)</span></div><div class='line' id='LC602'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">saveNTuplesSkimLoose</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;keep  floats_singleTopMCTopsNeutrino_*_*&#39;</span><span class="p">)</span></div><div class='line' id='LC603'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">saveNTuplesSkimLoose</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;keep  floats_singleTopMCTopsQuark_*_*&#39;</span><span class="p">)</span></div><div class='line' id='LC604'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">saveNTuplesSkimLoose</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;keep  floats_singleTopMCTopsQuarkBar_*_*&#39;</span><span class="p">)</span></div><div class='line' id='LC605'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#Higgs</span></div><div class='line' id='LC606'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">saveNTuplesSkimLoose</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;keep  floats_singleTopMCHiggs_*_*&#39;</span><span class="p">)</span></div><div class='line' id='LC607'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">saveNTuplesSkimLoose</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;keep  floats_singleTopMCHiggsBQuark_*_*&#39;</span><span class="p">)</span></div><div class='line' id='LC608'><br/></div><div class='line' id='LC609'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC610'><span class="c">## Output module configuration</span></div><div class='line' id='LC611'><span class="n">process</span><span class="o">.</span><span class="n">singleTopNTupleOut</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">OutputModule</span><span class="p">(</span></div><div class='line' id='LC612'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;PoolOutputModule&quot;</span><span class="p">,</span></div><div class='line' id='LC613'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fileName</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">untracked</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&#39;singleTopEdmNtuple_&#39;</span><span class="o">+</span><span class="n">ChannelName</span><span class="o">+</span><span class="s">&#39;.root&#39;</span><span class="p">),</span></div><div class='line' id='LC614'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring(&#39;preselection&#39;)),</span></div><div class='line' id='LC615'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">outputCommands</span> <span class="o">=</span> <span class="n">saveNTuplesSkimLoose</span><span class="p">,</span></div><div class='line' id='LC616'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC617'><br/></div><div class='line' id='LC618'><span class="n">process</span><span class="o">.</span><span class="n">singleTopNTupleOut</span><span class="o">.</span><span class="n">dropMetaData</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">untracked</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="s">&quot;ALL&quot;</span><span class="p">)</span></div><div class='line' id='LC619'><br/></div><div class='line' id='LC620'><span class="n">process</span><span class="o">.</span><span class="n">outpath</span> <span class="o">=</span> <span class="n">cms</span><span class="o">.</span><span class="n">EndPath</span><span class="p">(</span></div><div class='line' id='LC621'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">singleTopPatTuple</span> <span class="o">+</span></div><div class='line' id='LC622'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">process</span><span class="o">.</span><span class="n">singleTopNTupleOut</span></div><div class='line' id='LC623'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC624'><br/></div></pre></div>
            </td>
          </tr>
        </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.05828s from github-fe132-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/oiorio/cmssw/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

  </body>
</html>

