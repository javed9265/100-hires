# Cold Email Deliverability in 2026: The New Rules (Avoid Spam Folders)
*Expert:* Nick Abraham
*YouTube:* https://www.youtube.com/watch?v=h2j0gFz9RH4
*Published:* 2026-02-23

## Key Takeaways
- Deliverability is now a core part of cold outreach performance, not a technical afterthought.
- Authentication, infrastructure, sending behavior, and list quality all affect inbox placement.
- Teams should monitor spam risk before scaling outbound volume.
- Avoiding spam folders requires operational discipline across domains, inboxes, and copy.

---

## Full Transcript

[00:00] What is going on guys? It has been over
[00:02] a year since I posted on this channel,
[00:04] but I'm back and I'm back and motivated
[00:06] to talk about managing deliverability in
[00:08] 2026 as that has been a pretty hot
[00:11] topic. And I'm more motivated because my
[00:14] good friend Eric has been posting twice
[00:16] a day and has motivated me to get off my
[00:19] lazy ass and start recording videos just
[00:21] like I did a few years back. So, let's
[00:23] talk about managing deliverability in
[00:25] 2026. So, in our SmartLad account, uh, I
[00:29] wrote all this out about a month ago. We
[00:31] had we had about 126,000 email accounts.
[00:34] We're actually closer to 144,000 email
[00:36] accounts as of today. And managing all
[00:39] of that takes a lot of work and there's
[00:41] a lot of things that we've learned and
[00:42] processes we've built. So, I kind of
[00:44] want to go through that. Um, so if
[00:46] you're interested, sit back, watch, and
[00:48] let's go through it. So, from an
[00:50] infrastructure standpoint, I'm a big
[00:52] believer of always sending from Google
[00:54] or Microsoft accounts. Anybody that I've
[00:56] seen doing well with SMTP always comes
[00:59] back in three months and says this is
[01:01] not working anymore. It seems like
[01:02] anytime there's a huge like I would say
[01:05] like spam filter update of some sort, um
[01:08] SMTPs fuel the burn more than Google and
[01:10] Microsoft do and just generally they
[01:13] perform better and have like way less
[01:16] variance in results. Um that's how I've
[01:19] always seen it from SMTP. So whenever
[01:21] you're buying your accounts, always buy
[01:23] from providers that are using Google or
[01:25] Microsoft. And then with the domains,
[01:28] like the TLD doesn't really matter that
[01:29] much. Like stick toss when possible.
[01:31] Like there's, you know, sales that are
[01:33] on pork bun. You know, you you can gets
[01:35] for way cheaper during these sales
[01:37] periods through these domain registars.
[01:39] So try to get dots, but we also
[01:41] use.org.info.co
[01:43] andbiz because they are cheaper. Um, the
[01:45] thing to keep in mind though is I do
[01:47] feel like they burn out a little quicker
[01:49] and and my thought process here is it's
[01:52] because it does look a little bit more
[01:53] spammy and so like you may have an
[01:55] additional person or two that marks it
[01:57] as fan span should because of that. Uh,
[01:59] but that's just kind of more of a
[02:00] thought process less than like you know
[02:01] I've done the testing and I figured that
[02:03] out. Uh, with warm-up, we recommend a
[02:06] minimum of 2 weeks. And, you know, with
[02:09] running Allegian agencies, clients want
[02:11] to get campaigns launched as soon as
[02:13] possible. And so, we're kind of forced
[02:15] to do a minimum of two weeks. But for a
[02:18] couple of our clients, we actually
[02:20] launched probably after like a month and
[02:21] a half of warm-up. And we saw those
[02:23] domains perform so much better and
[02:26] probably last a lot longer as well. But,
[02:29] you know, for most of you guys, you're
[02:30] kind of running in a crunch. So, there's
[02:32] not much to do there. And then a big
[02:34] thing I'm a believer in is kind of like
[02:35] a rotation strategy. So for every
[02:38] client, you want to buy two sets of
[02:39] infra infra in infrastructure. One that
[02:41] you use in month one and then the second
[02:43] one they use in month two. And then you
[02:45] just rotate A and B. And it's super easy
[02:47] to do this if you have a subscription
[02:49] like Hyperype for example. you can use
[02:52] their bulk uh tag updator to basically
[02:55] give half of your inboxes group A and
[02:58] your other half as group B and then you
[03:00] can assign all the inboxes to a client
[03:02] and then in smart lead it's really easy
[03:03] to filter for the client and then for
[03:06] the tag and then whenever it comes to
[03:08] like naming conventions of uh campaigns
[03:10] you could say like you know client name
[03:14] campaign industry the date that you
[03:17] launched the campaign and then the group
[03:19] that it's in. And so then you can kind
[03:20] of assess like okay like did the
[03:23] campaign do good because of the industry
[03:25] or because of deliverability or like if
[03:28] this is a proven industry with a proven
[03:29] offer and group B did bad then it's
[03:32] probably the infra issue. So it gets way
[03:33] easier to point things out like that and
[03:35] just like be able to look at an overview
[03:36] and identify things when you have it set
[03:37] up like that. Um and then if you're
[03:40] running a legion agency, I feel like a
[03:42] lot of you guys watching this probably
[03:43] run legion agencies. Um, I I highly
[03:46] recommend just having a ton of
[03:47] non-branded domains that you just have
[03:49] in the backup. And and what you can do
[03:51] here is like if your main info ever goes
[03:53] down for a client, you can swap in the
[03:55] emergency domains. And regardless of
[03:58] what provider you use, uh, we use
[04:00] hypertide. Other people will use inbox
[04:03] kit or scaled mail. There's they're all
[04:05] pretty much all the same in my opinion.
[04:06] It just comes down to customer support
[04:08] and pricing. Uh, which is where you
[04:10] should kind of identify like, you know,
[04:11] what does better or whatnot. Uh, but all
[04:14] of them at scale will somehow always
[04:16] mess up and and like this this is going
[04:18] to happen regardless, right? They're
[04:19] going to mess up the
[04:22] DNS settings here and there, right? And
[04:24] so, you always just want to make sure
[04:25] you're on your tippy toes when it comes
[04:26] to that. And so, I always recommend you
[04:28] guys sending yourself a test email and
[04:30] checking the headers before you take any
[04:31] campaign live. Uh, because that that
[04:33] stuff is like a automatic, you know,
[04:36] you're going to go to the spam if you
[04:37] don't have that set up correctly. So,
[04:39] uh, that is a one very large thing to do
[04:41] on the DNS side. So that's that's
[04:43] everything infrastructure related. Let's
[04:44] talk about campaign setup. So most of
[04:48] you guys know this, but do not track
[04:50] open. Open data is unreliable and it can
[04:53] hurt your delivery with your format.
[04:55] Just keep it plain text and very simple.
[04:58] No fancy formatting. You want it to kind
[05:00] of look like a natural email so that it
[05:03] avoids a spam filter. And then for for
[05:05] timing, um I always recommend
[05:09] just sending through the the regular
[05:10] time zones of Monday to Friday, 9 to5.
[05:13] What we like to do inside of Smartly is
[05:14] use their API and basically update the
[05:17] start time and the end time every day on
[05:19] every campaign and randomize it plus or
[05:21] 30 minutes uh or plus or minus in
[05:25] between 30 minutes of the original
[05:26] launch time that we had. Super easy
[05:28] automation you could set up. And we do
[05:31] find that Saturdays are a good day to
[05:33] perform specifically when you're hitting
[05:34] like SMBs or midmarket. So that's
[05:36] something that you might want to
[05:36] consider. And then even on holidays,
[05:39] like people turn off their campaigns. I
[05:40] recommend you keep it on. Like most of
[05:42] our clients are targeting SMBs or
[05:44] mid-market. And like you know, I'm
[05:46] technically a small business owner. I
[05:48] check my emails every single day, every
[05:50] morning. That's like my first thing I
[05:51] do, check my emails. That's how it is
[05:53] with most business owners. And so you
[05:55] shouldn't feel like you can't email them
[05:58] on a Saturday or a holiday. And you
[06:01] know, you could say, "Oh, that's
[06:02] unprofessional, whatever." But it works.
[06:04] Like some of the holidays is some of the
[06:06] days we generate the most leads for
[06:07] clients. And so would highly recommend
[06:10] that. And then when it comes to the the
[06:12] lead list, couple things that I've
[06:13] noticed. One is you need to make sure
[06:16] that you format the company names
[06:17] properly. And ideally, you just don't
[06:19] use the company name at all. I find that
[06:21] whenever we have company name or title
[06:23] name inside of the campaign, we tend to
[06:26] find that it does worse. But like if you
[06:28] are going to use it, make sure that it's
[06:30] formatted properly. And like same thing
[06:32] with the titles, like you have to use AI
[06:34] to basically format it to be more uh
[06:38] normalized. So what I mean by that is
[06:39] like you're not going to ever go up to
[06:40] someone and say, "Hey, I noticed you
[06:42] you're the chief executive officer."
[06:43] You're always going to say, "I noticed
[06:45] that you were the CEO." Right? And so
[06:47] you have to catch those nuances. And
[06:49] like that's an easy example, but there's
[06:51] some titles that are pretty lengthy that
[06:53] AI sometimes can't normalize and like
[06:55] you wouldn't go there and call them
[06:57] like, "Hey, I saw that you know you're
[06:59] the director of intelligence." Um, and
[07:02] then whatever, right? Like bad example,
[07:04] but you get my point. And then the other
[07:06] thing too is I would recommend that you
[07:09] just remove all email sec people on your
[07:13] lead list that have email security,
[07:15] right? So you could use Google's three
[07:17] DNS endpoint to identify anybody that
[07:19] has like Proof Point, Barracuda, Mcast,
[07:21] any of those SCGs on your leave list,
[07:24] and I would just remove them. And if
[07:26] that makes your leave list super small,
[07:27] I recommend that you just put them at
[07:30] the end of your lead list. And a good
[07:31] way to do this is through a free tool
[07:33] that actually Omare dropped um last week
[07:36] on his website. It's
[07:37] hyperlist.hypertai.io,
[07:40] I think, something like that. go to his
[07:41] LinkedIn, you'll find it and that'll
[07:43] help you sort the list at the bottom.
[07:46] And then um when it comes to ISPs as
[07:49] well, a good thing I've noticed as well
[07:52] is when people isolate ISPs, you usually
[07:55] find that your domain gets flagged way
[07:56] quicker. So like if you remove all the
[07:58] Outlooks, you remove all the SMTPs and
[08:01] anyone else on your lead list and you
[08:02] just hammer Google. And let's say you're
[08:04] not using a ton of domains, you're not
[08:05] using a ton of spin tax, your domain
[08:07] will absolutely get flagged and every
[08:08] email you send to Google will get
[08:10] rejected. And so I do not recommend just
[08:12] isolating one provider and then and then
[08:15] doing nothing else. Um, and that happens
[08:17] when you send like a lot of volume and
[08:19] like your sequencer is kind of sending a
[08:21] majority of its volume in short blasts.
[08:24] That's whenever that happens. So that's
[08:25] something to kind of keep in mind as
[08:26] well. And then make sure you validate
[08:28] your email list with any one of the
[08:30] email validation tools. There's a
[08:31] million of them out there. We use
[08:32] million verifier. I love their API. We
[08:34] don't find that it has errors as often
[08:37] as some of the others. And yeah, like I
[08:39] I would always validate regardless if my
[08:42] because like if you look at any data
[08:43] provider, they all tell you, you know,
[08:45] emails are 90% valid or 95% valid. And
[08:48] and I never believe that. You always
[08:49] want to validate right before you launch
[08:50] the campaign. And that's a good practice
[08:52] to always have. And if you're going to
[08:55] validate your catch alls, you know, use
[08:56] scrubby, use bounce band. It doesn't
[08:58] matter which one you use, but catch alls
[09:00] typically will always have a higher
[09:02] bounce rate. And so what I recommend you
[09:05] doing is separating your campaigns. You
[09:08] should have one for your bow emails and
[09:10] then one for your valid catcholes. And
[09:12] you can moderate easier and turn off a
[09:16] campaign because with catchpholes, it's
[09:18] really hard to validate the the way that
[09:20] SMTPs are validated. And so you're going
[09:22] to find yourself having a lot of false
[09:24] positives. And so it's easier to just be
[09:27] able to see two campaigns. One is having
[09:29] a massive bounce rate. It's the cashall
[09:30] one. Let me go pause that campaign and
[09:32] not start sending to the rest of the
[09:33] cash on there so that I don't wreck my
[09:36] deliverability. That's something that I
[09:37] recommend you doing on the leadless
[09:40] level. Now with copyright, um the big
[09:43] things I would recommend is spin tax
[09:46] everything. But the the key here is you
[09:49] need to review all the different
[09:51] variants and read it out yourself. Like,
[09:53] and a lot of people don't do that. They
[09:54] just use AI to spin tax it and then they
[09:56] just kind of let it run. But here's the
[09:57] thing, AI will mess up. It will come up
[10:00] with some variants that just don't sound
[10:01] normal at all. And that will kill your
[10:03] performance, not the deliverability,
[10:05] like it having the weird spin tax
[10:07] errors. And so, just make sure you
[10:10] review the spin tax um with your copy.
[10:13] Make sure you keep it simple. no images,
[10:15] PDFs, or links in the first email. I've
[10:17] never seen that work consistently. Like,
[10:20] you may be able to run a few campaigns
[10:22] and have a better reply rate in the
[10:24] short term, but if you're trying to
[10:25] manage deliverability at scale, it's not
[10:28] worth it. But if you're like, yo, like
[10:30] if it gets me better results and I can,
[10:32] you know, allocate a bigger budget to
[10:34] infra and just be okay with it
[10:36] constantly burning out, then that's the
[10:37] game you play. And that's totally okay.
[10:39] Uh, and it may work, right? And then
[10:42] with cold emails, like I read so many
[10:44] cold emails and I think to myself, why
[10:46] would you say this? Right? Like it needs
[10:49] to pass the test of one, can a
[10:52] 10-year-old read this and know exactly
[10:54] what you're selling? And then two, it
[10:56] needs to be something that you would
[10:57] actually say to someone else in person.
[10:59] Like we have customers that sell
[11:01] solutions where it's like
[11:03] like you make this sound like something
[11:05] super complicated and crazy when it's
[11:09] not that. app. Like we had a customer
[11:10] that literally will pull put like a like
[11:14] it's kind of like a a Google or a search
[11:16] bar at the bottom of your websites and
[11:19] um it allows you to like like basically
[11:21] the the offer here is like you know B2B
[11:24] buyers will come to uh your website and
[11:27] just scan if they can't find your
[11:29] information they will just dip off your
[11:31] site. But like if you have a search
[11:33] board they can just ask the question and
[11:34] find the the relevant answer. So, kind
[11:37] of a cool value prop. And the copy that
[11:39] they wanted us to run was like talking
[11:41] about like conversion rates and talking
[11:44] about like, you know, uh how it helps
[11:47] with AI SEO and all this like craziness.
[11:50] And they had some technical terms in
[11:51] there. And I was like, dude, you
[11:53] literally need to just say, "Hey, look,
[11:54] I find that a lot of B2B buyers are
[11:56] bouncing off of sites because they scan
[11:58] it and can't find the answers to their
[11:59] questions quickly. We could add a search
[12:02] bar at the bottom of your page that's
[12:05] accessible and it drives up conversions
[12:06] because it leads them right to the
[12:08] answer that they're looking for. Is that
[12:10] something you'd be interested in? Like,
[12:12] you know, it's it's that simple. You
[12:13] just have to make it conversational. Um,
[12:16] and then when it comes to
[12:17] personalization,
[12:19] I I'm a huge believer in personalization
[12:22] can help a weak offer slightly perform
[12:24] better, but it still will be the reason
[12:26] that your campaign scales. And so people
[12:29] overobsess on personalization. But if
[12:31] you had two options, having a 10 out of
[12:34] 10 personalized campaign or a campaign
[12:37] with no personalization, but a great
[12:38] offer, the great offer will always
[12:40] outperform the personalization. So
[12:43] instead of trying to figure out the
[12:44] 10step clay workflow to create the best
[12:46] personalization in the world, figure out
[12:48] how to make your offer better. and and
[12:50] when you have a better offer and you
[12:52] start to get more replies to your
[12:53] campaign, your deliverability is much
[12:56] easier to manage than the guy that gets
[12:58] zero responses to his campaign. So
[13:00] that's everything I would keep in mind
[13:01] for for uh copyrightiting. And now when
[13:04] it comes to actually measuring
[13:06] deliverability, um everyone has like
[13:08] their own tips and points to it. I you
[13:11] know this is what we have started we've
[13:13] started doing in Q4 that has made our
[13:15] lives a lot easier. Um, it's so much
[13:17] easier to do now today than ever before.
[13:20] Slight mostly because of of three
[13:22] reasons. One, hikerite has really good
[13:24] APIs that we're able to use that allow
[13:26] us to build a lot of the dashboards that
[13:28] we want. Smartle has a lot of APIs that
[13:30] we're able to use that help us also to
[13:32] build really cool dashboards. And then
[13:35] Lovable has made it to where we can
[13:37] build dashboards really quickly. So, I
[13:39] would say it's it's a contribution to
[13:41] those three tools. And what we do is
[13:44] we're trying to assess the domain reply
[13:48] rate comparative to the client's offer.
[13:50] And so let me explain that and and my
[13:51] thought process behind it. Like I could
[13:55] say that I want all my clients to get a
[13:57] 3% reply rate because that's the average
[14:00] we're getting for the month or whatever
[14:02] it is, right? But sometimes it's
[14:04] impossible to get a client to get to
[14:06] there because of who they're selling to
[14:09] and the the offer that they have. And so
[14:12] it's unfair to think that there's a
[14:14] deliverability issue on these domains
[14:16] when in reality it's more of an offer
[14:18] and market issue. And so like we have
[14:21] clients that are getting great results
[14:23] and they have a 1% reply rate. But but
[14:26] since they're not hitting that 3% reply
[14:28] rate that we have as an agency average,
[14:30] like we think to ourselves that there's
[14:31] a deliverability issue when there isn't.
[14:33] And so I think it's so much smarter and
[14:35] better to compare the individual domain
[14:38] reply rate to the overall average that
[14:40] the client is gay. And so you can kind
[14:41] of see that in the screenshot right
[14:43] here. Let me zoom in real quick for you
[14:45] guys.
[14:47] You'll see right here, we basically have
[14:49] all of the domains and the reply rates.
[14:52] And this is the client's overall average
[14:53] reply rate. And we're looking at each
[14:56] individual domain's reply rate and
[14:57] seeing what percentage different is the
[15:01] domain comparative to the average. And
[15:03] if we see that a domain is doing 57% or
[15:06] worse or really like our rule is 40% or
[15:08] worse than the client average and is
[15:10] sent sufficient volume then we will mark
[15:13] it as questionable and then usually
[15:15] delete it and reorder it. So that's kind
[15:18] of how we think about deliverability um
[15:20] and and assessing deliverability. Um and
[15:24] and that's the key of it. Uh,
[15:30] and then I would say the other piece
[15:31] that is really useful because of
[15:33] hypertide is like how we're able to
[15:35] manage or replace domains better. And I
[15:38] really had this in my doc because I made
[15:39] the doc a month ago. So I'm stealing
[15:40] Omar's LinkedIn post. So this isn't the
[15:42] most I would say best YouTube video or
[15:44] anything by any means, but it gets the
[15:46] job done. Anyways, basically what we do
[15:49] is use hypertide relay. So, what they've
[15:51] built is a way for you to delete your
[15:53] domain, but then still be able to get
[15:55] all the replies that come to this domain
[15:57] to a preset inbox that you have. And so,
[16:00] let me kind of explain where this is
[16:01] really good. And and it kind of goes in
[16:03] tangent with uh another one of their
[16:08] solutions, which is
[16:11] I got pause real quick.
[16:14] I believe they call it hypertide
[16:16] layover. So, basically like let's say we
[16:19] have a campaign, right? and it's doing
[16:20] 40% worse uh on a domain level. On that
[16:24] domain, we can actually cancel it. And
[16:26] what they do is they give you an 18-day
[16:28] grace period. So even though I delete it
[16:29] today, it's not going to delete or it's
[16:31] not going to be removed until day 18.
[16:35] And so I can still be sending from that
[16:36] inbox for the next 18 days. And what's
[16:39] good about that is that we don't have
[16:41] clients that have lower volume because
[16:43] their infra is, you know, completely
[16:45] gone and deleted. And what we can do is
[16:47] set up new infra on day one. Use the
[16:50] layover to cancel the domain. So it gets
[16:52] removed from our billing, but it's still
[16:54] active and sending. And then when we
[16:56] cancel it, we can set up the relay,
[16:58] which is now going to say, okay, on day
[16:59] 18, when this inbox actually gets
[17:01] deleted, and you know, I've been sending
[17:02] from day one all the way to day 18, all
[17:04] the people that reply to your inbox from
[17:06] that day 18 is going to get forwarded to
[17:08] your new inbox that you set up. And like
[17:11] that's beautiful. That's amazing. So now
[17:13] we have like kind of like a
[17:14] self-evolving deliverability management
[17:16] system to make sure that we never run
[17:18] into issues at scale. And that's all you
[17:21] really have to do to manage
[17:22] deliverability in 2026. People will tell
[17:25] you that there's some crazy new hack or
[17:27] crazy new strategy or something that you
[17:29] need to be on the watch for, but this is
[17:31] it. And this is just like relentless
[17:34] execution of the fundamentals. And so
[17:37] that's that. But it wouldn't be me if I
[17:39] didn't pitch Lee. So, you know, if you
[17:41] guys need help with Legion, feel free to
[17:43] book a call with us at le.io
[17:46] and we will help you out. But that's it.
